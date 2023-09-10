import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip
import webbrowser  # Import modul webbrowser

# Fungsi S-DES Encryption
def sdes_encrypt(plaintext, key):
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

        print("Ronde 1:", subkey1)  # Menampilkan subkey 1
        print("Ronde 2:", subkey2)  # Menampilkan subkey 2

        return subkey1, subkey2

    # Fungsi untuk melakukan F-function pada plain_text dan subkey
    def f_function(plain_text, subkey):
        plain_text = permute(plain_text, EP)
        xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(plain_text, subkey))
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

    # Fungsi utama enkripsi
    def encrypt(plain_text, key):
        subkey1, subkey2 = generate_subkeys(key)

        # Initial Permutation
        plain_text = permute(plain_text, IP)

        # First Round
        left_half = plain_text[:4]
        right_half = plain_text[4:]
        f_result = f_function(right_half, subkey1)
        left_half = ''.join(str(int(a) ^ int(b)) for a, b in zip(left_half, f_result))

        # Swap left and right halves
        left_half, right_half = right_half, left_half

        # Second Round
        f_result = f_function(right_half, subkey2)
        left_half = ''.join(str(int(a) ^ int(b)) for a, b in zip(left_half, f_result))

        # Inverse Initial Permutation
        cipher_text = permute(left_half + right_half, IP_INV)
        return cipher_text

    # Padding plaintext jika kurang dari 8 bit
    if len(plaintext) < 8:
        plaintext = plaintext.zfill(8)

    # Lakukan enkripsi menggunakan S-DES
    ciphertext = encrypt(plaintext, key)
    return ciphertext

# Fungsi untuk mengenkripsi saat tombol "Encrypt" diklik
def encrypt_button_clicked():
    plaintext = plaintext_entry.get()
    key = key_entry.get()

    # Periksa apakah input adalah angka biner (hanya mengandung 0 dan 1)
    if not (plaintext.isdigit() and all(char in '01' for char in plaintext)) or \
       not (key.isdigit() and all(char in '01' for char in key)):
        messagebox.showerror("Error", "Input harus berupa angka biner (hanya mengandung 0 dan 1)")
        return

    # Periksa panjang plaintext dan kunci
    if len(plaintext) != 8:
        messagebox.showerror("Error", "Plaintext harus 8 bit biner")
        return

    if len(key) != 10:
        messagebox.showerror("Error", "Kunci harus 10 bit biner")
        return

    # Padding plaintext jika kurang dari 8 bit
    if len(plaintext) < 8:
        plaintext = plaintext.zfill(8)

    # Lakukan enkripsi menggunakan S-DES
    ciphertext = sdes_encrypt(plaintext, key)

    # Tampilkan hasil enkripsi dengan properti teks yang diubah
    result_label.config(
        text="Ciphertext: " + ciphertext,
        foreground="red",
        font=("Arial", 12, "bold"),
        justify="center",
        anchor="center"
    )

    # Menampilkan tombol "Copy Hasil"
    copy_button.grid(row=4, column=0, columnspan=2, pady=(10, 20), sticky=tk.NSEW)

# Fungsi untuk mereset input dan hasil
def reset_button_clicked():
    plaintext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result_label.config(text="", foreground="black", font=("Arial", 10), relief="flat")
    copy_button.grid_remove()

# Fungsi untuk menyalin hasil ke clipboard
def copy_button_clicked():
    ciphertext = result_label.cget("text")
    pyperclip.copy(ciphertext)
    messagebox.showinfo("Info", "Hasil enkripsi telah disalin ke clipboard")

# Membuat jendela utama
window = tk.Tk()
window.title("S-DES Encryption")

# Membuat input untuk Plaintext
plaintext_label = ttk.Label(window, text="Plaintext (8 bit):")
plaintext_label.grid(row=0, column=0, sticky=tk.W)
plaintext_entry = ttk.Entry(window, justify="right")
plaintext_entry.grid(row=0, column=1)

# Membuat input untuk Kunci
key_label = ttk.Label(window, text="Kunci (10 bit):")
key_label.grid(row=1, column=0, sticky=tk.W)
key_entry = ttk.Entry(window, justify="right")
key_entry.grid(row=1, column=1)

# Tombol "Encrypt" untuk memulai enkripsi
encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.grid(row=2, column=1, sticky=tk.E)

# Tombol "Reset" untuk mereset input dan hasil
reset_button = ttk.Button(window, text="Reset", command=reset_button_clicked)
reset_button.grid(row=2, column=0, sticky=tk.W)

# Label untuk menampilkan hasil enkripsi
result_label = ttk.Label(window, text="", foreground="black", font=("Arial", 10), relief="flat")
result_label.grid(row=3, columnspan=2, pady=(15, 5))

# Tombol "Copy Hasil" untuk menyalin hasil enkripsi ke clipboard (dibuat terlebih dahulu tetapi tidak ditampilkan)
copy_button = ttk.Button(window, text="Copy Hasil", command=copy_button_clicked)
copy_button.grid(row=5, column=0, columnspan=2, pady=(20, 10), sticky=tk.NSEW)
copy_button.grid_remove()

# Menambahkan keterangan hak cipta di tengah bawah
copyright_label = ttk.Label(window, text="© 2023 BukanMakmum.", foreground="gray", cursor="hand2")
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
