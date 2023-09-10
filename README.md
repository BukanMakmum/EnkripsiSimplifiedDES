# Enkripsi dan Dekripsi S-DES

Repository ini berisi skrip Python untuk melakukan enkripsi dan dekripsi S-DES menggunakan antarmuka pengguna grafis (GUI) yang dibangun dengan Tkinter. S-DES (Simplified Data Encryption Standard) adalah versi yang disederhanakan dari algoritma Data Encryption Standard (DES).

## Isi

1. [Pendahuluan](#pendahuluan)
2. [Ketergantungan](#ketergantungan)
3. [Penggunaan](#penggunaan)
4. [Tangkapan Layar](#tangkapan-layar)
5. [Lisensi](#lisensi)
6. [Kontak](#kontak)

## Pendahuluan

S-DES (Simplified Data Encryption Standard) adalah cipher blok kunci simetris yang beroperasi pada blok data kecil. Ini menggunakan kunci 10 bit untuk mengenkripsi dan mendekripsi plaintext atau ciphertext 8 bit. Repositori ini menyediakan skrip Python untuk melakukan enkripsi dan dekripsi S-DES.

Repository ini berisi dua skrip:
- `Enkripsi.py`: Skrip ini memungkinkan Anda untuk mengenkripsi plaintext 8 bit menggunakan kunci 10 bit.
- `Dekripsi.py`: Skrip ini memungkinkan Anda untuk mendekripsi ciphertext 8 bit menggunakan kunci 10 bit.

Kedua skrip ini mencakup antarmuka pengguna grafis (GUI) yang dibangun dengan Tkinter untuk kemudahan penggunaan.

## Ketergantungan

Library Python berikut diperlukan untuk menjalankan skrip:
- `tkinter`: Digunakan untuk membangun antarmuka pengguna grafis (GUI).
- `pyperclip`: Digunakan untuk menyalin hasil ke clipboard.
- `webbrowser`: Digunakan untuk membuka tautan alamat email.

## Penggunaan

### Enkripsi

Untuk melakukan enkripsi S-DES, ikuti langkah-langkah berikut:

1. Jalankan skrip `Enkripsi.py`.
2. Masukkan plaintext 8 bit dalam kolom input "Plaintext (8 bit)".
3. Masukkan kunci 10 bit dalam kolom input "Kunci (10 bit)".
4. Klik tombol "Encrypt" untuk melakukan enkripsi.
5. Ciphertext akan ditampilkan dalam area hasil.
6. Anda dapat mengklik tombol "Salin Hasil" untuk menyalin ciphertext ke clipboard.

### Dekripsi

Untuk melakukan dekripsi S-DES, ikuti langkah-langkah berikut:

1. Jalankan skrip `Dekripsi.py`.
2. Masukkan ciphertext 8 bit dalam kolom input "Ciphertext (8 bit)".
3. Masukkan kunci 10 bit dalam kolom input "Kunci (10 bit)".
4. Klik tombol "Decrypt" untuk melakukan dekripsi.
5. Plaintext akan ditampilkan dalam area hasil.
6. Anda dapat mengklik tombol "Salin Hasil" untuk menyalin plaintext ke clipboard.

## Tangkapan Layar

![Hasil](https://github.com/BukanMakmum/EnkripsiSimplifiedDES/assets/32379649/92cbe6b5-621c-4181-b350-a9176ede6115)


## Lisensi

Projek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
