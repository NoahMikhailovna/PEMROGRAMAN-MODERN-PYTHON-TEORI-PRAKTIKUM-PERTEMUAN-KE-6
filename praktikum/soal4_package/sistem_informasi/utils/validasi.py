"""Validasi sederhana untuk entitas Mahasiswa."""


def validasi_mahasiswa(mahasiswa):
    """Return (is_valid, errors) untuk objek Mahasiswa."""
    errors = []
    if not mahasiswa.nim or len(str(mahasiswa.nim)) < 5:
        errors.append("NIM tidak valid (minimal 5 karakter)")
    if not mahasiswa.nama or len(mahasiswa.nama.strip()) < 3:
        errors.append("Nama tidak valid (minimal 3 karakter)")
    if not 0.0 <= mahasiswa.ipk <= 4.0:
        errors.append("IPK harus di rentang 0.0 - 4.0")
    if mahasiswa.status not in ("Aktif", "Cuti", "Lulus", "Nonaktif"):
        errors.append("Status harus Aktif/Cuti/Lulus/Nonaktif")
    return len(errors) == 0, errors


if __name__ == "__main__":
    # Jalankan sebagai module dari folder soal4_package:
    #   python -m sistem_informasi.utils.validasi
    from sistem_informasi.model.mahasiswa import Mahasiswa

    print(validasi_mahasiswa(Mahasiswa("001", "Bu")))
