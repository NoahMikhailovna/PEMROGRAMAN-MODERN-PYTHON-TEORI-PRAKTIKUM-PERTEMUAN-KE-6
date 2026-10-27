"""
Soal Praktik 1: Fungsi hitung_statistik().

Menerima list angka, mengembalikan dictionary berisi:
mean, median, modus, range (max-min), dan standard deviation.
Hanya memakai standard library: statistics dan math.
"""

import math
import statistics


def hitung_statistik(data):
    """
    Menghitung statistik deskriptif dari list angka.

    Args:
        data (list): list berisi angka (int/float), tidak boleh kosong.

    Returns:
        dict: {"mean", "median", "modus", "range", "standar_deviasi"}

    Raises:
        ValueError: jika data kosong.
        TypeError: jika ada elemen yang bukan angka.
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")

    for item in data:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(f"Semua elemen harus angka, ditemukan: {item!r}")
        if isinstance(item, float) and math.isnan(item):
            raise ValueError("Data tidak boleh mengandung NaN")

    # Modus: statistics.mode melempar StatisticsError bila tidak ada modus
    # tunggal (semua nilai unik / seri), fallback ke nilai pertama terbanyak.
    try:
        modus = statistics.mode(data)
    except statistics.StatisticsError:
        modus = statistics.multimode(data)[0]

    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": modus,
        "range": max(data) - min(data),
        # pstdev = standar deviasi populasi (data dianggap keseluruhan populasi)
        "standar_deviasi": statistics.pstdev(data) if len(data) > 1 else 0.0,
    }


if __name__ == "__main__":
    nilai = [85, 90, 78, 92, 88, 85, 90, 85]
    print("=== Soal 1: hitung_statistik() ===")
    print(f"Data: {nilai}")

    hasil = hitung_statistik(nilai)
    for kunci, nilai_hasil in hasil.items():
        if isinstance(nilai_hasil, float):
            print(f"  {kunci:<16}: {nilai_hasil:.2f}")
        else:
            print(f"  {kunci:<16}: {nilai_hasil}")

    print(f"\nData kedua: {[70, 80, 90, 100, 80]}")
    print(" ", hitung_statistik([70, 80, 90, 100, 80]))

    try:
        hitung_statistik([])
    except ValueError as e:
        print(f"\nData kosong -> ValueError: {e}")
