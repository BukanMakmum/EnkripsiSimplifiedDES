import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip
import webbrowser  # Import modul webbrowser

# Fungsi S-DES Decryption
def sdes_decrypt(ciphertext, key):
    # Inisialisasi tabel substitusi dan tabel permutasi
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    P4 = [2, 4, 3, 1]
    S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]
    S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

    # Helper function untuk melakukan permutasi
    def permute(input_text, permutation_table):
        return ''.join(input_text[i - 1] for i in permutation_table)

    # Helper function untuk melakukan left shift pada string
    def left_shift(input_text, shifts):
        return input_text[shifts:] + input_text[:shifts]

    # Fungsi untuk menghasilkan subkeys
    def generate_subkeys(key):
        key = permute(key, P10)
        key_left = key[:5]
        key_right = key[5:]
        key_left_shifted = left_shift(key_left, 1)
        key_right_shifted = left_shift(key_right, 1)
        subkey1 = permute(key_left_shifted + key_right_shifted, P8)

        key_left_shifted = left_shift(key_left_shifted, 2)
        key_right_shifted = left_shift(key_right_shifted, 2)
        subkey2 = permute(key_left_shifted + key_right_shifted, P8)

        print("Subkey 1:", subkey1)
        print("Subkey 2:", subkey2)

        return subkey1, subkey2

    # Fungsi untuk melakukan F-function pada ciphertext dan subkey
    def f_function(ciphertext, subkey):
        ciphertext = permute(ciphertext, EP)
        xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(ciphertext, subkey))
        left_half = xor_result[:4]
        right_half = xor_result[4:]
        row1 = int(left_half[0] + left_half[3], 2)
        col1 = int(left_half[1] + left_half[2], 2)
        row2 = int(right_half[0] + right_half[3], 2)
        col2 = int(right_half[1] + right_half[2], 2)
        s0_value = S0[row1][col1]
        s1_value = S1[row2][col2]
        s_result = bin(s0_value)[2:].zfill(2) + bin(s1_value)[2:].zfill(2)
        p4_result = permute(s_result, P4)
        return p4_result

    # Fungsi utama dekripsi
    def decrypt(ciphertext, key):
        subkey1, subkey2 = generate_subkeys(key)

        # Initial Permutation
        ciphertext = permute(ciphertext, IP)

        # First Round
        left_half = ciphertext[:4]
        right_half = ciphertext[4:]
        f_result = f_function(right_half, subkey2)
        left_half = ''.join(str(int(a) ^ int(b)) for a, b in zip(left_half, f_result))

        # Swap left and right halves
        left_half, right_half = right_half, left_half

        # Second Round
        f_result = f_function(right_half, subkey1)
        left_half = ''.join(str(int(a) ^ int(b)) for a, b in zip(left_half, f_result))

        # Inverse Initial Permutation
        plaintext = permute(left_half + right_half, IP_INV)
        return plaintext

    # Padding ciphertext jika kurang dari 8 bit
    if len(ciphertext) < 8:
        ciphertext = ciphertext.zfill(8)

    # Lakukan dekripsi menggunakan S-DES
    plaintext = decrypt(ciphertext, key)
    return plaintext

# Fungsi untuk melakukan dekripsi saat tombol "Decrypt" diklik
def decrypt_button_clicked():
    ciphertext = ciphertext_entry.get()
    key = key_entry.get()

    # Periksa apakah input adalah angka biner (hanya mengandung 0 dan 1)
    if not (ciphertext.isdigit() and all(char in '01' for char in ciphertext)) or \
       not (key.isdigit() and all(char in '01' for char in key)):
        messagebox.showerror("Error", "Input harus berupa angka biner (hanya mengandung 0 dan 1)")
        return

    # Periksa panjang ciphertext dan kunci
    if len(ciphertext) != 8:
        messagebox.showerror("Error", "Ciphertext harus 8 bit biner")
        return

    if len(key) != 10:
        messagebox.showerror("Error", "Kunci harus 10 bit biner")
        return

    # Padding ciphertext jika kurang dari 8 bit
    if len(ciphertext) < 8:
        ciphertext = ciphertext.zfill(8)

    # Lakukan dekripsi menggunakan S-DES
    plaintext = sdes_decrypt(ciphertext, key)

    # Tampilkan hasil dekripsi dengan properti teks yang diubah
    result_label.config(
        text="Plaintext: " + plaintext,
        foreground="blue",
        font=("Arial", 12, "bold"),
        justify="center",  # Mengatur rata tengah horizontal
        anchor="center"    # Mengatur rata tengah vertical
    )

    # Menampilkan tombol "Copy Hasil"
    copy_button.grid(row=4, column=0, columnspan=2, pady=(10, 20), sticky=tk.NSEW)

    # Menghilangkan box border pada hasil
    result_frame.config(borderwidth=0, relief="flat")

# Fungsi untuk mereset input dan hasil
def reset_button_clicked():
    ciphertext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result_label.config(text="", foreground="black", font=("Arial", 10))
    copy_button.grid_remove()  # Menghilangkan tombol "Copy Hasil" saat hasil dihapus atau direset

# Fungsi untuk menyalin hasil ke clipboard
def copy_button_clicked():
    plaintext = result_label.cget("text")
    pyperclip.copy(plaintext)  # Menyalin plaintext ke clipboard
    messagebox.showinfo("Info", "Hasil dekripsi telah disalin ke clipboard")

# Membuat jendela utama
window = tk.Tk()
window.title("S-DES Decryption")

# Membuat input untuk Ciphertext
ciphertext_label = ttk.Label(window, text="Ciphertext (8 bit):")
ciphertext_label.grid(row=0, column=0, sticky=tk.W)
ciphertext_entry = ttk.Entry(window, justify="right")
ciphertext_entry.grid(row=0, column=1)

# Membuat input untuk Kunci
key_label = ttk.Label(window, text="Kunci (10 bit):")
key_label.grid(row=1, column=0, sticky=tk.W)
key_entry = ttk.Entry(window, justify="right")
key_entry.grid(row=1, column=1)

# Tombol "Decrypt" untuk memulai dekripsi
decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.grid(row=2, column=1, sticky=tk.E)

# Tombol "Reset" untuk mereset input dan hasil
reset_button = ttk.Button(window, text="Reset", command=reset_button_clicked)
reset_button.grid(row=2, column=0, sticky=tk.W)

# Label untuk menampilkan hasil dekripsi dalam frame
result_frame = ttk.Frame(window, padding=(5, 5, 5, 5))
result_frame.grid(row=3, columnspan=2, sticky=tk.NSEW, pady=(10, 0))

result_label = ttk.Label(result_frame, text="", foreground="black", font=("Arial", 10))
result_label.pack(fill="both", expand=True)

# Tombol "Copy Hasil" untuk menyalin hasil dekripsi ke clipboard (dibuat terlebih dahulu tetapi tidak ditampilkan)
copy_button = ttk.Button(window, text="Copy Hasil", command=copy_button_clicked)
copy_button.grid(row=4, column=0, columnspan=2, pady=(20, 10), sticky=tk.NSEW)
copy_button.grid_remove()  # Menyembunyikan tombol "Copy Hasil" saat awal aplikasi

# Menambahkan keterangan hak cipta di tengah bawah
copyright_label = ttk.Label(window, text="© 2023 @BukanMakmum.", foreground="gray", cursor="hand2")
copyright_label.grid(row=5, column=0, columnspan=2, pady=(0, 10), sticky=tk.NSEW)

# Mengatur teks hak cipta menjadi rata tengah horizontal
copyright_label.configure(anchor="center", justify="center")

# Fungsi untuk mengarahkan ke alamat email saat teks hak cipta diklik
def open_email(event):
    webbrowser.open("mailto:imamsayuti.usk@gmail.com")

# Menghubungkan fungsi dengan klik pada teks hak cipta
copyright_label.bind("<Button-1>", open_email)

# Menjalankan loop utama GUI
window.mainloop()
