"""
Teori 3: Pitfall objek mutable sebagai default parameter.

Nilai default dievaluasi SEKALI saat fungsi didefinisikan.
List/dict yang sama dipakai semua pemanggilan -> data bocor antar panggilan.
Solusi: gunakan None sebagai sentinel, buat objek baru di dalam fungsi.
"""


# SALAH: keranjang=[] hanya dibuat satu kali
def tambah_item_salah(item, keranjang=[]):
    keranjang.append(item)
    return keranjang


# BENAR: None sebagai sentinel
def tambah_item_benar(item, keranjang=None):
    if keranjang is None:
        keranjang = []
    keranjang.append(item)
    return keranjang


if __name__ == "__main__":
    print("=== Teori 3: Mutable Default Pitfall ===")
    print("\nCara SALAH (default = []):")
    print("  tambah_item_salah('apel')  ->", tambah_item_salah("apel"))
    print("  tambah_item_salah('jeruk') ->", tambah_item_salah("jeruk"),
          " <- 'apel' ikut terbawa!")

    print("\nCara BENAR (default = None):")
    print("  tambah_item_benar('apel')  ->", tambah_item_benar("apel"))
    print("  tambah_item_benar('jeruk') ->", tambah_item_benar("jeruk"),
          " <- bersih, list baru")
