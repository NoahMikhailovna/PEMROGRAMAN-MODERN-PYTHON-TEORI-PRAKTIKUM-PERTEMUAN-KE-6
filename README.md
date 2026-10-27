# Pemrograman Modern Python — Teori & Praktikum Pertemuan ke-6

**Topik:** Function, Parameter, Return Value, Scope, Lambda, Module, Package & Library

- **Nama:** Fakhry Ahmad Fauzan
- **NPM:** 20241320038

## Isi Repository

### 1. Teori — folder `teori/`
- `Jawaban_Teori.md` — jawaban tertulis 5 soal teori (parameter vs argumen, LEGB, pitfall mutable default, module vs package, lambda vs def). Soal teori dijawab tertulis, tanpa file kode terpisah.

### 2. Praktikum — folder `praktikum/`
| Soal | Folder / File | Keterangan |
|---|---|---|
| 1 | `soal1_hitung_statistik.py` | Fungsi `hitung_statistik()` — mean, median, modus, range, standar deviasi (hanya `statistics` & `math`) |
| 2 | `soal2_validasi_data.py` | Fungsi `validasi_data()` — validasi dict terhadap schema, return `(is_valid, errors)`, memakai `*args` & `**kwargs` |
| 3 | `soal3_module/` | Module `utilitas_akademik.py` (`hitung_ipk`, `konversi_nilai_huruf`, `generate_transkrip`) + `main.py` yang mengimpornya |
| 4 | `soal4_package/` | Package `sistem_informasi` (subpackage `model`, `service`, `utils`) — CRUD Mahasiswa in-memory + `main.py` demo |
| 5 | `soal5_api/` | `analisis_api.py` — ambil data JSONPlaceholder pakai `requests`, proses dengan lambda + `map`/`filter`/`sorted`, simpan hasil ke `hasil_analisis.json` |

### 3. Screenshot Hasil Praktikum — folder `screenshot_hasil_praktikum/`
Screenshot output saat kode praktikum dijalankan, satu file per soal praktikum (soal 1-5).

## Cara Menjalankan

```bash
python praktikum/soal1_hitung_statistik.py
python praktikum/soal2_validasi_data.py
python praktikum/soal3_module/main.py
python praktikum/soal4_package/main.py
pip install -r requirements.txt
python praktikum/soal5_api/analisis_api.py
```
