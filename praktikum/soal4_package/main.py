"""
Soal Praktik 4 (main): demo package sistem_informasi.

Menjalankan CRUD Mahasiswa: Create, Read, Update, Delete.
Jalankan dari folder ini:  python main.py
"""

from sistem_informasi import Mahasiswa, MahasiswaService
from sistem_informasi.utils.formatter import format_tabel


def main():
    print("=== Soal 4: Package sistem_informasi (CRUD Mahasiswa) ===")
    service = MahasiswaService()

    print("\n[CREATE]")
    for mhs in [
        Mahasiswa("20241320038", "Fakhry Ahmad Fauzan", ipk=3.75),
        Mahasiswa("20241320039", "Ani Rahmawati", ipk=3.90),
        Mahasiswa("20241320040", "Budi Santoso", ipk=3.40),
    ]:
        print(" ", service.tambah(mhs)[1])
    print("  Tambah duplikat:", service.tambah(Mahasiswa("20241320038", "Ganda"))[1])

    print("\n[READ - semua]")
    print(format_tabel(service.ambil_semua()))
    print("\n[READ - satu] ambil NIM 20241320039:")
    print(" ", service.ambil("20241320039"))
    print("[CARI] nama mengandung 'ani':", [str(m) for m in service.cari("ani")])

    print("\n[UPDATE] IPK Budi -> 3.60, status tetap Aktif:")
    print(" ", service.ubah("20241320040", ipk=3.60)[1])
    print(" ", service.ambil("20241320040"))

    print("\n[DELETE] hapus NIM 20241320040:")
    print(" ", service.hapus("20241320040")[1])
    print(f"  Jumlah akhir: {service.jumlah()} mahasiswa")
    print(format_tabel(service.ambil_semua()))


if __name__ == "__main__":
    main()
