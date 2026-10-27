"""
Teori 5: Lambda vs def.

Lambda tepat untuk: key sorted/min/max, map/filter sederhana, callback singkat.
def tepat untuk: logika multi-baris, fungsi yang dipakai ulang & diberi nama jelas,
fungsi yang butuh docstring / pengujian / penanganan error.
"""


# def: bernama, bisa multi-baris, punya docstring
def kategorikan_ipk(ipk):
    """Mengembalikan predikat berdasarkan IPK. Logika bercabang seperti
    ini TIDAK bisa ditulis sebagai lambda."""
    if ipk >= 3.5:
        return "Cumlaude"
    if ipk >= 3.0:
        return "Sangat Memuaskan"
    if ipk >= 2.5:
        return "Memuaskan"
    return "Perlu Perbaikan"


# lambda: anonim, satu ekspresi
kuadrat = lambda x: x ** 2  # noqa: E731 - sengaja untuk contoh teori


if __name__ == "__main__":
    print("=== Teori 5: Lambda vs def ===")
    print(f"Lambda kuadrat(5) = {kuadrat(5)}")

    mahasiswa = [
        {"nama": "Budi", "ipk": 3.75},
        {"nama": "Ani", "ipk": 3.90},
        {"nama": "Cici", "ipk": 3.60},
        {"nama": "Dani", "ipk": 2.40},
    ]

    # Lambda sebagai key pada sorted()
    print("\nDiurutkan IPK tertinggi (lambda sebagai key sorted):")
    for m in sorted(mahasiswa, key=lambda m: m["ipk"], reverse=True):
        print(f"  {m['nama']}: {m['ipk']} -> {kategorikan_ipk(m['ipk'])} (pakai def)")

    # Lambda pada map() dan filter()
    nilai = [78, 85, 92, 67, 90]
    print(f"\nNilai asal        : {nilai}")
    print(f"map lambda /100   : {list(map(lambda x: x / 100, nilai))}")
    print(f"filter lambda >=80: {list(filter(lambda x: x >= 80, nilai))}")
