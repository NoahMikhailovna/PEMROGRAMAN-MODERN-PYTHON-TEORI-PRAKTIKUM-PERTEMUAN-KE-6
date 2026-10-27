# Jawaban Soal Teori — Pertemuan 6
## Function, Parameter, Return Value, Scope, Lambda, Module, Package & Library

**Nama:** Fakhry Ahmad Fauzan — **NPM:** 20241320038

---

## 1. Perbedaan Parameter dan Argumen

**Parameter** adalah variabel yang ditulis pada **definisi fungsi** (di dalam tanda kurung setelah nama fungsi). Parameter hanyalah *placeholder* / penampung — ia belum memiliki nilai nyata, ia hanya menyatakan data apa saja yang dibutuhkan fungsi.

**Argumen** adalah **nilai aktual** yang diberikan saat fungsi **dipanggil**. Nilai inilah yang kemudian mengisi parameter.

Analogi: parameter adalah kolom kosong pada formulir, argumen adalah data yang diisikan ke kolom tersebut.

```python
# harga dan tarif adalah PARAMETER (ditulis saat definisi)
def hitung_pajak(harga, tarif=0.11):
    return harga * tarif

# 100000 dan 0.11 adalah ARGUMEN (diberikan saat pemanggilan)
pajak1 = hitung_pajak(100000, 0.11)        # argumen positional
pajak2 = hitung_pajak(harga=100000)        # argumen keyword, tarif memakai default
```

| Aspek | Parameter | Argumen |
|---|---|---|
| Ditulis di | Definisi fungsi (`def`) | Pemanggilan fungsi |
| Sifat | Placeholder / variabel | Nilai aktual |
| Contoh | `harga`, `tarif` | `100000`, `0.11` |
| Jumlah diketahui | Saat fungsi dibuat | Saat fungsi dipakai |

---

## 2. Aturan LEGB dalam Scope Python

LEGB adalah urutan pencarian nama variabel oleh Python ketika sebuah nama dipakai. Python mencari dari lingkup paling dalam ke paling luar, dan berhenti pada lingkup pertama yang menemukan nama tersebut. Jika tidak ditemukan di semua level, terjadi `NameError`.

1. **L — Local**: variabel yang didefinisikan di dalam fungsi yang sedang berjalan. Masa hidupnya hanya selama fungsi dieksekusi.
   - Contoh situasi: variabel `hasil` di dalam `def hitung(): hasil = a + b`.
2. **E — Enclosing**: variabel dari fungsi luar yang membungkus fungsi dalam (*nested function / closure*). Bukan lokal fungsi dalam, bukan pula global.
   - Contoh situasi: fungsi `dalam()` membaca variabel `x` milik fungsi `luar()` yang membungkusnya.
3. **G — Global**: variabel yang didefinisikan di tingkat modul (di luar semua fungsi). Bisa dibaca dari mana saja di modul tersebut; untuk *mengubahnya* dari dalam fungsi perlu keyword `global`.
   - Contoh situasi: konstanta `KAMPUS = "UKRI"` di baris atas file yang dibaca banyak fungsi.
4. **B — Built-in**: nama bawaan Python yang selalu tersedia tanpa didefinisikan, misalnya `print`, `len`, `range`, `max`, `Exception`.
   - Contoh situasi: memanggil `len("halo")` — `len` ditemukan di level Built-in karena tidak ada di Local/Enclosing/Global.

```python
x = "global"                 # Global

def luar():
    x = "enclosing"          # Enclosing
    def dalam():
        x = "local"          # Local
        print(x)             # -> local
        print(len("halo"))   # len -> Built-in
    dalam()
    print(x)                 # -> enclosing

luar()
print(x)                     # -> global
```

Catatan: menimpa nama built-in (misalnya `len = 5`) disebut *shadowing* dan harus dihindari karena `len()` setelah itu tidak bisa dipakai lagi.

---

## 3. Pitfall Objek Mutable sebagai Default Parameter

**Mekanisme:** nilai default parameter **dievaluasi hanya satu kali, saat fungsi didefinisikan** — bukan setiap kali fungsi dipanggil. Jika nilai default itu objek *mutable* (bisa diubah di tempat) seperti `list`, `dict`, atau `set`, maka objek yang sama dipakai bersama oleh semua pemanggilan. Perubahan pada pemanggilan pertama (misalnya `append`) akan "bocor" dan terlihat pada pemanggilan berikutnya, padahal pemanggil mengira ia mendapat objek baru yang kosong.

```python
# SALAH
def tambah_item(item, keranjang=[]):
    keranjang.append(item)
    return keranjang

print(tambah_item("apel"))    # ['apel']
print(tambah_item("jeruk"))   # ['apel', 'jeruk']  <- BUKAN ['jeruk']!
```

**Solusi yang benar:** pakai `None` sebagai nilai penanda (*sentinel*), lalu buat objek baru di dalam badan fungsi. `None` bersifat immutable dan hanya dipakai sebagai tanda "belum diberikan".

```python
# BENAR
def tambah_item(item, keranjang=None):
    if keranjang is None:
        keranjang = []
    keranjang.append(item)
    return keranjang

print(tambah_item("apel"))    # ['apel']
print(tambah_item("jeruk"))   # ['jeruk']  <- benar, list baru setiap panggilan
```

---

## 4. Perbedaan Module dan Package, serta Peran `__init__.py`

**Module** adalah **satu file** Python (`.py`) yang berisi fungsi, kelas, dan variabel. Setiap file `.py` otomatis menjadi module, dan namanya adalah nama file tanpa ekstensi. Module diimpor dengan `import nama_file`.

**Package** adalah **satu folder (direktori)** yang berisi kumpulan module (dan boleh berisi sub-package) yang saling berhubungan. Package memungkinkan hierarki dengan notasi titik, misalnya `sistem_informasi.service.mahasiswa_service`. Jadi: module = file, package = folder berisi module-module.

| Aspek | Module | Package |
|---|---|---|
| Bentuk fisik | File `.py` | Direktori / folder |
| Isi | Fungsi, kelas, variabel | Banyak module + sub-package |
| Penanda | Ekstensi `.py` | File `__init__.py` di dalamnya |
| Contoh | `math`, `json`, `utilitas_akademik.py` | `sistem_informasi/`, `pandas`, `numpy` |

**Peran `__init__.py`:**
1. **Penanda package** — memberi tahu Python bahwa folder tersebut adalah package yang bisa diimpor (untuk *regular package*).
2. **Kode inisialisasi** — kode di dalamnya dijalankan saat package pertama kali diimpor (misalnya menetapkan `__version__`).
3. **Mengontrol ekspor** — variabel `__all__` menentukan nama apa saja yang diimpor saat `from package import *`.
4. **Mempermudah import** — nama yang didefinisikan/diimpor di `__init__.py` bisa diakses langsung dari package, misalnya `from sistem_informasi import MahasiswaService` tanpa menyebut subpackage-nya.

> Contoh package nyata ada di Soal Praktik 4 (`praktikum/soal4_package/sistem_informasi/`).

---

## 5. Kapan Menggunakan Lambda, Kapan Menggunakan `def`

Lambda adalah fungsi anonim satu ekspresi: `lambda parameter: ekspresi`. Hasil ekspresi langsung dikembalikan tanpa kata `return`. Setiap lambda bisa ditulis ulang sebagai `def`, jadi pilihannya adalah soal keterbacaan dan kebutuhan.

**Lambda lebih tepat pada:**
1. **Sebagai `key` pada `sorted()` / `min()` / `max()`** — fungsi pengurutan singkat sekali pakai.
   `sorted(mahasiswa, key=lambda m: m["ipk"], reverse=True)`
2. **Sebagai argumen `map()` / `filter()` untuk transformasi sederhana satu baris.**
   `list(map(lambda x: x / 100, nilai))`
3. **Callback singkat sekali pakai** — misalnya pada event handler / GUI atau `reduce()` untuk operasi dua nilai yang sangat sederhana, di mana memberi nama fungsi justru menambah keruwetan.

**`def` lebih tepat pada:**
1. **Logika multi-baris / multi-statement** — ada percabangan, perulangan, atau beberapa langkah; lambda tidak bisa menampung statement.
2. **Fungsi yang dipakai ulang di banyak tempat dan perlu nama yang jelas** — nama fungsi yang deskriptif membuat kode dan pesan error (`traceback`) mudah dipahami.
3. **Fungsi yang butuh dokumentasi dan pengujian** — `def` bisa memiliki *docstring*, anotasi tipe, dekorator, dan diuji dengan unit test; lambda anonim tidak bisa didokumentasikan dengan baik. Lambda juga tidak cocok untuk rekursi dan logika dengan penanganan error (`try/except`).

