Tentu, berikut adalah `README.md` berdasarkan koding yang telah Anda berikan dalam bahasa Indonesia dan dengan lisensi GNU General Public License (GPL):

```markdown
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
pip install pyperclip
```

## Penggunaan
1. Jalankan skrip `sdes_gui.py`.
2. Masukkan pesan teks (desimal) dan kunci (desimal) ke dalam kolom input yang sesuai.
3. Klik tombol "Enkripsi" untuk melakukan enkripsi.
4. Aplikasi akan menampilkan kunci putaran, representasi biner dari pesan teks dan kunci, teks sandi (biner), dan teks sandi (desimal).
5. Anda dapat menyalin kunci putaran dan teks sandi ke clipboard menggunakan tombol "Salin" yang disediakan.

## Tangkapan Layar
![Hasil](https://github.com/BukanMakmum/EnkripsiSimplifiedDES/assets/32379649/40d3d80b-b109-4c78-85dd-bdbc275051a8)

## Lisensi
Proyek ini dilisensikan di bawah GNU General Public License (GPL). Lihat berkas [LICENSE](LICENSE) untuk rincian lebih lanjut.
```
