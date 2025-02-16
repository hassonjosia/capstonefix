from tabulate import tabulate
from datetime import datetime, timedelta
# data dummy 
rekrutmen = [
    {"ID": 1, "Nama": "Stario", "Posisi": "Software Engineer - Staff", "Scoring": 85, "Status": "Diterima", "Jadwal Wawancara": (datetime.now() + timedelta(weeks=1)).strftime('%Y-%m-%d')},
    {"ID": 2, "Nama": "Rodhi", "Posisi": "Data Analyst - Manager", "Scoring": 92, "Status": "Diterima", "Jadwal Wawancara": (datetime.now() + timedelta(weeks=1)).strftime('%Y-%m-%d')},
    {"ID": 3, "Nama": "Adrain", "Posisi": "HR Specialist - Staff", "Scoring": 40, "Status": "Ditolak", "Jadwal Wawancara": "-"},
    {"ID": 4, "Nama": "Idha", "Posisi": "UI/UX Designer - Staff", "Scoring": 0, "Status": "Menunggu Review", "Jadwal Wawancara": "TBD"}
]

# untuk menampilkan data rekrutmen
def show():
    print(tabulate(rekrutmen, headers="keys", tablefmt="grid"))
    input("\nTekan Enter untuk kembali ke menu utama...")

# untuk menambah rekrutmen 
def add():
    id = rekrutmen[-1]["ID"] + 1 if rekrutmen else 1
    nama = input("Masukkan Nama: ").capitalize()
    posisi = input("Masukkan Posisi: ")
    
    while True:
        level = input("Masukkan Level (Staff/Manager): ").strip().capitalize()
        if level in ["Staff", "Manager"]:
            break
        print("Input tidak valid! Harap masukkan 'Staff' atau 'Manager'.")
    
    posisiFinal = f"{posisi} - {level}"
    rekrutmen.append({"ID": id, "Nama": nama, "Posisi": posisiFinal, "Scoring": 0, "Status": "Menunggu Review", "Jadwal Wawancara": "TBD"})
    print("Pelamar berhasil ditambahkan!\n")
    input("\nTekan Enter untuk kembali ke menu utama...")

# untuk mengupdate
def update():
    while True:
        print("\nData Rekrutmen Saat Ini:")
        print(tabulate(rekrutmen, headers="keys", tablefmt="grid"))
        print("\n1. Update Scoring dan Status")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            # loop untuk mastiin id pelamar berupa angka yang valid
            id = None
            while id is None:
                inputId = input("Masukkan ID Pelamar: ")
                if inputId.isdigit():  # mastiin input adalah angka
                    id = int(inputId)
                else:
                    print("ID Pelamar harus berupa angka, harap coba lagi.")
            
            # cek apakah id pelamar ada dalam data
            pelamarDitemukan = False
            for x in rekrutmen:
                if x["ID"] == id:
                    pelamarDitemukan = True
                    break
            
            if not pelamarDitemukan:
                print("ID Pelamar tidak ditemukan! Coba lagi.")
                input("\nTekan Enter untuk melanjutkan...")
                continue  # ke loop dan meminta id pelamar lagi
            
            while True:
                try:
                    scoring = int(input("Masukkan Scoring (1-100): "))
                    if 1 <= scoring <= 100:
                        break
                    else:
                        print("Input tidak valid! Harap masukkan angka antara 1 dan 100.")
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka antara 1 dan 100.")
            
            # mengupdate score dan status pelamar
            for x in rekrutmen:
                if x["ID"] == id:
                    level = "Manager" if "Manager" in x["Posisi"] else "Staff"
                    minScore = 85 if level == "Manager" else 70
                    status = "Diterima" if scoring >= minScore else "Ditolak"
                    x["Scoring"] = scoring
                    x["Status"] = status

                    # untuk update  jadwal
                    if x["Status"] == "Diterima":
                        interview_date = datetime.now() + timedelta(weeks=1)  # Tambahkan seminggu
                        x["Jadwal Wawancara"] = interview_date.strftime('%Y-%m-%d')  # Format tanggal
                    elif x["Status"] == "Ditolak":
                        x["Jadwal Wawancara"] = "-"  # Jika ditolak, set "-"
                    elif x["Status"] == "Menunggu Review":
                        x["Jadwal Wawancara"] = "TBD"  # Jika menunggu review, set "TBD"
                    
                    print("Scoring dan Status berhasil diperbarui!\n")
                    input("\nTekan Enter untuk kembali ke menu utama...")
                    return
        elif pilihan == "2":
            return
        else:
            print("Pilihan tidak valid, coba lagi.")


# untuk menghapus pelamar
def delete():
    global rekrutmen
    
    while True:
        if not rekrutmen:
            print("\nData kosong!")
            input("\nTekan Enter untuk kembali ke menu utama...")
            return
        
        print("\nData Rekrutmen Saat Ini:")
        print(tabulate(rekrutmen, headers="keys", tablefmt="grid"))
        print("\n1. Hapus Pelamar")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            id = None
            while id is None:
                inputId = input("Masukkan ID Pelamar: ")
                if inputId.isdigit():  # mastiin input adalah angka
                    id = int(inputId)
                else:
                    print("ID Pelamar harus berupa angka, harap coba lagi.")

            # cek apakah id pelamar ada dalam data
            pelamarDitemukan = False
            for x in rekrutmen:
                if x["ID"] == id:
                    pelamarDitemukan = True
                    break

            if not pelamarDitemukan:
                print("ID Pelamar tidak ditemukan! Coba lagi.")
                input("\nTekan Enter untuk melanjutkan...")
                continue  # ke loop dan meminta id pelamar lagi
            
            for x in rekrutmen:
                if x["ID"] == id:
                    while True:
                        konfirmasi = input("Apakah Anda yakin ingin menghapus? (1: Setuju, 2: Kembali): ")
                        if konfirmasi == "1":
                            rekrutmen = [p for p in rekrutmen if p["ID"] != id]
                            print("Pelamar berhasil dihapus!\n")
                            if not rekrutmen:
                                print("Semua data telah dihapus. Data kosong!")
                                input("\nTekan Enter untuk kembali ke menu utama...")
                                return
                            
                            input("\nTekan Enter untuk kembali ke menu utama...")
                            return
                        elif konfirmasi == "2":
                            return delete()
                        else:
                            print("Pilihan tidak valid, coba lagi.")
            print("Pelamar tidak ditemukan!\n")
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == "2":
            return
        else:
            print("Pilihan tidak valid, coba lagi.")


# menu utama
def menu():
    while True:
        print("\n=== Sistem Rekrutmen Karyawan ===")
        print("1. Tampilkan Data Rekrutmen")
        print("2. Tambah Pelamar Baru")
        print("3. Update Status")
        print("4. Hapus Pelamar")
        print("5. Exit")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            show()
        elif pilihan == "2":
            add()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            print("Goodbye")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()
