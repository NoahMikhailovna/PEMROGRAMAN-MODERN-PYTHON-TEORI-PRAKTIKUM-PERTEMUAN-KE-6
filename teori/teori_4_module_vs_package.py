"""
Teori 4: Module vs Package.

Module  = satu file .py (misal: math, json, file ini sendiri).
Package = satu folder berisi module-module + file __init__.py
          (misal: collections adalah package/module bawaan,
           praktikum/soal4_package/sistem_informasi adalah package buatan sendiri).
Peran __init__.py: penanda package, kode inisialisasi, mengatur __all__,
dan tempat mengekspos nama agar mudah diimpor.
"""

import json  # json adalah module dari standard library
import math  # math adalah module

# collections adalah package standard library, Counter adalah salah satu isinya
from collections import Counter


if __name__ == "__main__":
    print("=== Teori 4: Module vs Package ===")
    print(f"Module math : sqrt(144) = {math.sqrt(144)}, pi = {math.pi:.4f}")
    print(f"Module json : dumps     = {json.dumps({'nama': 'Fakhry', 'ipk': 3.75})}")

    frek = Counter(["kopi", "teh", "kopi", "kopi", "teh"])
    print(f"Package collections.Counter: {dict(frek)}")

    print(f"Nama module ini (__name__): {__name__}")
    import os

    print(f"File module ini (__file__): {os.path.basename(__file__)}")
    print()
    print("Kesimpulan: module = 1 file .py, package = folder berisi")
    print("module-module yang ditandai dengan __init__.py.")
