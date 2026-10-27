"""
Soal Praktik 2: Fungsi validasi_data().

Menerima dictionary data dan schema validasi, mengembalikan
tuple (is_valid: bool, errors: list).

Format schema per field:
    {
        "tipe": str/int/float,   # tipe data yang diharapkan
        "wajib": True/False,     # field harus ada (default False)
        "min": angka,            # nilai minimum (untuk angka)
        "max": angka,            # nilai maksimum (untuk angka)
        "min_panjang": int,      # panjang minimum (untuk str/list)
        "max_panjang": int,      # panjang maksimum (untuk str/list)
        "pilihan": [...],        # nilai harus salah satu dari list ini
    }

*args   : nama field tambahan yang dianggap wajib di luar schema.
**kwargs: opsi tambahan, misal strict=True (field di luar schema = error).
"""


def validasi_data(data, schema, *args, **kwargs):
    """
    Memvalidasi data terhadap schema.

    Returns:
        tuple: (True, []) jika valid, atau (False, [pesan error, ...]).
    """
    strict = kwargs.get("strict", False)
    errors = []

    if not isinstance(data, dict):
        return False, ["Data harus berupa dictionary"]

    # Field wajib tambahan dari *args
    for field_wajib in args:
        if field_wajib not in data:
            errors.append(f"Field '{field_wajib}' wajib diisi (dari *args)")

    for field, aturan in schema.items():
        wajib = aturan.get("wajib", False)

        if field not in data:
            if wajib:
                errors.append(f"Field '{field}' wajib diisi")
            continue

        nilai = data[field]
        tipe = aturan.get("tipe")

        # Cek tipe (bool adalah subclass int di Python, harus ditolak untuk int)
        if tipe is not None:
            if tipe is int and isinstance(nilai, bool):
                errors.append(f"Field '{field}' harus bertipe int, bukan bool")
                continue
            # int diterima untuk field float (misal ipk = 3 dianggap 3.0)
            tipe_ok = isinstance(nilai, tipe) or (tipe is float and isinstance(nilai, int))
            if not tipe_ok:
                errors.append(
                    f"Field '{field}' harus bertipe {tipe.__name__}, "
                    f"ditemukan {type(nilai).__name__}"
                )
                continue  # cek lain tidak bermakna bila tipe sudah salah

        # Cek rentang nilai angka
        if isinstance(nilai, (int, float)) and not isinstance(nilai, bool):
            if "min" in aturan and nilai < aturan["min"]:
                errors.append(f"Field '{field}' = {nilai} di bawah minimum {aturan['min']}")
            if "max" in aturan and nilai > aturan["max"]:
                errors.append(f"Field '{field}' = {nilai} di atas maksimum {aturan['max']}")

        # Cek panjang str/list
        if isinstance(nilai, (str, list)):
            if "min_panjang" in aturan and len(nilai) < aturan["min_panjang"]:
                errors.append(f"Field '{field}' minimal {aturan['min_panjang']} karakter/item")
            if "max_panjang" in aturan and len(nilai) > aturan["max_panjang"]:
                errors.append(f"Field '{field}' maksimal {aturan['max_panjang']} karakter/item")

        # Cek pilihan
        if "pilihan" in aturan and nilai not in aturan["pilihan"]:
            errors.append(f"Field '{field}' harus salah satu dari {aturan['pilihan']}")

    # Mode strict: field yang tidak dikenal di schema adalah error
    if strict:
        for field in data:
            if field not in schema and field not in args:
                errors.append(f"Field '{field}' tidak dikenal dalam schema (strict)")

    return (len(errors) == 0), errors


if __name__ == "__main__":
    schema_mahasiswa = {
        "nama": {"tipe": str, "wajib": True, "min_panjang": 3, "max_panjang": 50},
        "nim": {"tipe": str, "wajib": True, "min_panjang": 8, "max_panjang": 15},
        "umur": {"tipe": int, "min": 17, "max": 60},
        "ipk": {"tipe": float, "min": 0.0, "max": 4.0},
        "status": {"tipe": str, "pilihan": ["Aktif", "Cuti", "Lulus", "Nonaktif"]},
    }

    print("=== Soal 2: validasi_data() ===")

    data_valid = {
        "nama": "Fakhry Ahmad Fauzan", "nim": "20241320038",
        "umur": 20, "ipk": 3.75, "status": "Aktif",
    }
    print("\nData valid:")
    print(" ", validasi_data(data_valid, schema_mahasiswa))

    data_invalid = {
        "nama": "Fa", "nim": "20241320038",
        "umur": 15, "ipk": 4.50, "status": "Libur",
    }
    valid, errors = validasi_data(data_invalid, schema_mahasiswa, "email", strict=False)
    print("\nData tidak valid (dengan field wajib tambahan 'email' via *args):")
    print(f"  is_valid = {valid}")
    for err in errors:
        print(f"  - {err}")
