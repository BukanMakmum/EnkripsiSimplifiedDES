# Enkripsi S-DES dengan Python dan Tkinter

Ini adalah implementasi sederhana dari algoritma Enkripsi Data Standard yang Disederhanakan (S-DES) menggunakan Python dan Tkinter untuk antarmuka pengguna grafis (GUI).

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Persyaratan](#persyaratan)
- [Penggunaan](#penggunaan)
- [Tangkapan Layar](#tangkapan-layar)
- [Lisensi](#lisensi)

## Deskripsi
S-DES adalah versi disederhanakan dari algoritma Data Encryption Standard (DES). Ini digunakan untuk melakukan enkripsi pada pesan teks biasa 8-bit dengan kunci 10-bit, menghasilkan teks sandi 8-bit.

Proyek ini menyediakan GUI yang ramah pengguna yang memungkinkan Anda untuk mengenkripsi pesan teks menggunakan S-DES dengan kunci yang ditentukan. Ini juga menampilkan representasi biner dari teks biasa, kunci, dan kunci putaran, bersama dengan teks sandi dalam format biner dan desimal.

## Persyaratan
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal Python dan pustaka-pustaka berikut:

- `tkinter`: Pustaka GUI standar Python.
- `pyperclip`: Untuk menyalin hasil ke clipboard.

Anda dapat menginstal `pyperclip` menggunakan pip:

```bash
python -m pip install tk
pip install pyperclip
```

## Penggunaan
1. Jalankan skrip `enkripsi.py`.
2. Masukkan pesan teks (biner dengan panjang 8 bit) dan kunci (biner dengan panjang 10 bit) ke dalam kolom input yang sesuai.
3. Klik tombol "Enkripsi" untuk melakukan enkripsi.
4. Aplikasi akan menampilkan kunci putaran, representasi biner dari pesan teks dan kunci, teks sandi (biner), dan teks sandi (desimal).
5. Anda dapat menyalin hasil/output ke clipboard menggunakan tombol "Copy Hasil" yang disediakan.

## Tangkapan Layar
![Output](https://github.com/BukanMakmum/EnkripsiSimplifiedDES/assets/32379649/e4459c06-ed26-400a-bf2e-22c8faf616e0)


![Hasil](https://github.com/BukanMakmum/EnkripsiSimplifiedDES/assets/32379649/3521431b-3290-4c84-b041-5a2fcff81c7c)




## Lisensi
Proyek ini dilisensikan di bawah GNU General Public License (GPL). Lihat berkas [LICENSE](LICENSE) untuk rincian lebih lanjut.

