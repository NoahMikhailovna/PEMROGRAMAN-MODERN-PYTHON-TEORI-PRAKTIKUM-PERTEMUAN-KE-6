"""
Soal Praktik 3 (module): utilitas_akademik.py

Module utilitas akademik berisi:
- konversi_nilai_huruf(): angka -> (huruf, bobot)
- hitung_ipk(): list mata kuliah -> IPK
- generate_transkrip(): data mahasiswa + nilai -> teks transkrip
"""

# Tabel bobot nilai huruf
BOBOT_HURUF = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}


def konversi_nilai_huruf(nilai_angka):
    """
    Mengonversi nilai angka (0-100) ke nilai huruf dan bobotnya.

    Returns:
        tuple: (huruf, bobot), contoh: (85 -> ("A", 4.0))
    """
    if not 0 <= nilai_angka <= 100:
        raise ValueError(f"Nilai harus 0-100, ditemukan {nilai_angka}")
    if nilai_angka >= 85:
        huruf = "A"
    elif nilai_angka >= 70:
        huruf = "B"
    elif nilai_angka >= 55:
        huruf = "C"
    elif nilai_angka >= 40:
        huruf = "D"
    else:
        huruf = "E"
    return huruf, BOBOT_HURUF[huruf]


def _bobot_dari_item(item):
    """Mengambil (sks, bobot) dari satu item mata kuliah.

    Item boleh berisi kunci 'nilai' (angka 0-100) atau 'huruf' (A-E).
    """
    sks = item.get("sks", 0)
    if "huruf" in item:
        return sks, BOBOT_HURUF[item["huruf"].upper()]
    _, bobot = konversi_nilai_huruf(item["nilai"])
    return sks, bobot


def hitung_ipk(daftar_nilai):
    """
    Menghitung IPK = sum(bobot x sks) / sum(sks).

    Args:
        daftar_nilai (list): list dict, contoh:
            {"mata_kuliah": "Pemrograman Python", "sks": 3, "nilai": 90}
            atau {"mata_kuliah": "...", "sks": 2, "huruf": "B"}

    Returns:
        float: IPK skala 0.00-4.00. 0.0 bila daftar kosong / total SKS 0.
    """
    total_bobot_x_sks = 0.0
    total_sks = 0
    for item in daftar_nilai:
        sks, bobot = _bobot_dari_item(item)
        total_bobot_x_sks += bobot * sks
        total_sks += sks
    if total_sks == 0:
        return 0.0
    return total_bobot_x_sks / total_sks


def generate_transkrip(mahasiswa, daftar_nilai):
    """
    Membuat teks transkrip sederhana.

    Args:
        mahasiswa (dict): {"nama": ..., "nim": ..., "jurusan": ...}
        daftar_nilai (list): format sama seperti hitung_ipk().

    Returns:
        str: teks transkrip yang sudah diformat.
    """
    baris = []
    baris.append("=" * 56)
    baris.append("TRANSKRIP NILAI MAHASISWA")
    baris.append("=" * 56)
    baris.append(f"Nama    : {mahasiswa.get('nama', '-')}")
    baris.append(f"NIM     : {mahasiswa.get('nim', '-')}")
    baris.append(f"Jurusan : {mahasiswa.get('jurusan', '-')}")
    baris.append("-" * 56)
    baris.append(f"{'Mata Kuliah':<32} {'SKS':>4} {'Nilai':>6} {'Huruf':>6}")
    baris.append("-" * 56)

    total_sks = 0
    for item in daftar_nilai:
        if "huruf" in item:
            huruf = item["huruf"].upper()
            tampil_nilai = "-"
        else:
            huruf, _ = konversi_nilai_huruf(item["nilai"])
            tampil_nilai = str(item["nilai"])
        total_sks += item.get("sks", 0)
        baris.append(
            f"{item.get('mata_kuliah', '-'):<32} {item.get('sks', 0):>4} "
            f"{tampil_nilai:>6} {huruf:>6}"
        )

    baris.append("-" * 56)
    baris.append(f"Total SKS : {total_sks}")
    baris.append(f"IPK       : {hitung_ipk(daftar_nilai):.2f}")
    baris.append("=" * 56)
    return "\n".join(baris)


if __name__ == "__main__":
    # Testing module ini bila dieksekusi langsung
    print("Testing utilitas_akademik.py:")
    print("  konversi 85 ->", konversi_nilai_huruf(85))
    print("  konversi 62 ->", konversi_nilai_huruf(62))
    contoh = [
        {"mata_kuliah": "Pemrograman Python", "sks": 3, "nilai": 90},
        {"mata_kuliah": "Basis Data", "sks": 3, "nilai": 78},
    ]
    print(f"  hitung_ipk(contoh) = {hitung_ipk(contoh):.2f}")
