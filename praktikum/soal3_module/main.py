"""
Soal Praktik 3 (main): main.py

Mengimpor dan menggunakan module utilitas_akademik.
Jalankan dari folder ini:  python main.py
"""

from utilitas_akademik import generate_transkrip, hitung_ipk, konversi_nilai_huruf


def main():
    mahasiswa = {
        "nama": "Fakhry Ahmad Fauzan",
        "nim": "20241320038",
        "jurusan": "Sistem Informasi",
    }
    daftar_nilai = [
        {"mata_kuliah": "Pemrograman Python", "sks": 3, "nilai": 90},
        {"mata_kuliah": "Basis Data", "sks": 3, "nilai": 84},
        {"mata_kuliah": "Sistem Informasi Manajemen", "sks": 2, "nilai": 76},
        {"mata_kuliah": "Statistika", "sks": 2, "nilai": 68},
        {"mata_kuliah": "Bahasa Inggris", "sks": 2, "huruf": "A"},
    ]

    print("=== Soal 3: Module utilitas_akademik ===")
    print("\nContoh konversi_nilai_huruf():")
    for angka in (90, 84, 76, 68, 35):
        huruf, bobot = konversi_nilai_huruf(angka)
        print(f"  {angka} -> {huruf} (bobot {bobot})")

    print(f"\nIPK dari hitung_ipk(): {hitung_ipk(daftar_nilai):.2f}\n")
    print(generate_transkrip(mahasiswa, daftar_nilai))


if __name__ == "__main__":
    main()
