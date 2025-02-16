# capstone
#Module 1 Capstone Project
##Sistem Rekrutmen Karyawan
Sistem ini memungkinkan pengguna untuk mengelola data rekrutmen karyawan dengan fitur untuk menampilkan data, menambah pelamar baru, memperbarui status pelamar, dan menghapus pelamar. Aplikasi ini menggunakan Python dan tabulate untuk menampilkan data dalam format tabel yang rapi.

##Fitur
1. Menampilkan Data Rekrutmen
Menampilkan seluruh data pelamar yang ada di sistem dalam format tabel.

2. Menambahkan Pelamar Baru
Menambah pelamar baru dengan memasukkan nama, posisi, dan level (Staff/Manager). Pelamar baru akan dimasukkan dengan status "Menunggu Review".

3. Memperbarui Status dan Scoring Pelamar
Memungkinkan pengguna untuk memperbarui nilai scoring (1-100) dan status pelamar berdasarkan nilai yang dimasukkan (status: "Diterima" atau "Ditolak").

4. Menghapus Pelamar
Menghapus pelamar dari data rekrutmen berdasarkan ID pelamar.

##Struktur Data
Data rekrutmen disimpan dalam list of dictionaries dengan format sebagai berikut:

`rekrutmen = [
    {"ID": 1, "Nama": "Nama Pelamar", "Posisi": "Posisi Pelamar - Level", "Scoring": Nilai Scoring, "Status": "Status Pelamar"}
]`

ID(int): ID unik untuk setiap pelamar.
Nama(string): Nama pelamar.
Posisi(string): Posisi yang dilamar dan level (Staff/Manager).
Scoring(int): Nilai yang diperoleh pelamar berdasarkan evaluasi (1-100).
Status: Status pelamar berdasarkan scoring (Diterima, Ditolak, Menunggu Review).

##Contoh Penggunaan
1. Menampilkan Data Rekrutmen
- Program akan menampilkan seluruh data rekrutmen dalam format tabel.

2. Menambah Pelamar Baru
- Anda akan diminta untuk memasukkan nama, posisi, dan level pelamar. Data baru akan ditambahkan dengan status "Menunggu Review".
  
3. Memperbarui Scoring dan Status
- Anda bisa memasukkan ID pelamar dan memberikan nilai scoring. Sistem akan mengupdate status pelamar sesuai dengan nilai yang dimasukkan.
  
4. Menghapus Pelamar
- Anda bisa menghapus pelamar berdasarkan ID. Setelah penghapusan, sistem akan meminta konfirmasi sebelum melanjutkan.

