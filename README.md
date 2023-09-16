# Enkripsi dan Dekripsi S-DES

Repository ini berisi source code Python untuk melakukan enkripsi dan dekripsi S-DES menggunakan antarmuka pengguna grafis (GUI) yang dibangun dengan Tkinter. S-DES (Simplified Data Encryption Standard) adalah versi yang disederhanakan dari algoritma Data Encryption Standard (DES). S-DES (Simplified Data Encryption Standard) Education merupakan source code yang dikembangkan untuk pembelajaran proses enkripsi dan dekripsi menggunakan S-DES.

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
- `DESv1.0.py atau sesuai versi`: Skrip ini memungkinkan Anda untuk mengenkripsi plaintext 8 bit dan mengdekripsi Ciphertext 8 bit menggunakan kunci 10 bit.

Kedua skrip ini mencakup antarmuka pengguna grafis (GUI) yang dibangun dengan Tkinter untuk kemudahan penggunaan.

## Ketergantungan

Library Python berikut diperlukan untuk menjalankan skrip:
- `tkinter`: Digunakan untuk membangun antarmuka pengguna grafis (GUI).
- `pyperclip`: Digunakan untuk menyalin hasil ke clipboard.
- `webbrowser`: Digunakan untuk membuka tautan alamat email.

## Penggunaan

### Enkripsi dan Dekripsi

Untuk melakukan Enkripsi dan Dekripsi S-DES, ikuti langkah-langkah berikut:

1. Jalankan skrip `DESv1.0.py atau sesuai versi`.
2. Masukkan plaintext 8 bit atau ciphertext 8 bit dalam kolom input "Plaintext/ciphertext (8 bit)".
3. Masukkan kunci 10 bit dalam kolom input "Kunci (10 bit)".
4. Klik tombol "Encrypt" atau "Decrypt" untuk melakukan enkripsi/dekripsi.
5. Ciphertext/plaintext akan ditampilkan dalam area hasil.
6. Anda dapat mengklik tombol "Salin Hasil" untuk menyalin ciphertext/plaintext ke clipboard.
7. Klik reset untuk mengapus input dan output secara cepat

### - Contoh Input dan Output
  ```bash
  Plaintext:   00000001
  Key:         1001011000
  Ciphertext:  01101010
   ```
## Tangkapan Layar

![Hasil](https://github.com/BukanMakmum/SimplifiedDES/assets/32379649/7c05bea0-789e-4953-9de8-23c20ef30926)



## Lisensi

Projek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
