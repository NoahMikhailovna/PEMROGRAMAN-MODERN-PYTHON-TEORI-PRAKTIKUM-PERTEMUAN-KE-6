"""
Teori 2: Aturan LEGB (Local, Enclosing, Global, Built-in).

Python mencari nama variabel dengan urutan: L -> E -> G -> B.
Berhenti di level pertama yang menemukan nama tersebut.
"""

x = "global"  # Global scope: di tingkat modul
counter = 0   # Global scope, akan diubah lewat keyword global


def luar():
    x = "enclosing"  # Enclosing scope: milik fungsi luar

    def dalam():
        x = "local"  # Local scope: milik fungsi dalam
        print(f"Dalam fungsi dalam : x = {x}")  # -> local
        # len tidak ada di L/E/G, ditemukan di Built-in scope
        print(f"Built-in len('halo'): {len('halo')}")

    dalam()
    print(f"Dalam fungsi luar  : x = {x}")  # -> enclosing


def tambah_counter():
    global counter  # tanpa keyword ini, akan jadi variabel lokal baru
    counter += 1


if __name__ == "__main__":
    print("=== Teori 2: Aturan LEGB ===")
    luar()
    print(f"Di tingkat modul   : x = {x}")  # -> global

    print(f"\nCounter awal (global): {counter}")
    tambah_counter()
    tambah_counter()
    print(f"Counter setelah 2x tambah_counter(): {counter}")
