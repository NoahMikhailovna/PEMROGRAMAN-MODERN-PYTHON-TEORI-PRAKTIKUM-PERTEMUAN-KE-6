"""
Teori 1: Perbedaan Parameter dan Argumen.

Parameter = variabel pada DEFINISI fungsi (placeholder).
Argumen   = nilai aktual pada PEMANGGILAN fungsi.
"""


# harga dan tarif adalah PARAMETER.
# tarif memiliki nilai default 0.11, jadi boleh tidak diisi saat pemanggilan.
def hitung_pajak(harga, tarif=0.11):
    """Menghitung pajak dari harga. harga & tarif = parameter."""
    return harga * tarif


def buat_profil(nama, umur, jurusan="Sistem Informasi"):
    """nama, umur, jurusan = parameter."""
    return f"{nama}, {umur} tahun, jurusan {jurusan}"


if __name__ == "__main__":
    print("=== Teori 1: Parameter vs Argumen ===")

    # 100000 dan 0.11 adalah ARGUMEN positional (berdasarkan urutan)
    print("Argumen positional :", hitung_pajak(100000, 0.11))

    # harga=100000 adalah ARGUMEN keyword, tarif memakai default
    print("Argumen keyword    :", hitung_pajak(harga=100000))

    # Argumen untuk parameter nama, umur, jurusan
    print("Profil 1           :", buat_profil("Fakhry", 20))
    print("Profil 2           :", buat_profil(nama="Ani", jurusan="Informatika", umur=21))

    print()
    print("Kesimpulan: parameter ditulis saat fungsi DIBUAT,")
    print("argumen diberikan saat fungsi DIPANGGIL.")
