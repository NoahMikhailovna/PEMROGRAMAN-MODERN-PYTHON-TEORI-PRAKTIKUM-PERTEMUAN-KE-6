"""
Soal Praktik 5: Ambil data dari public REST API dan analisis.

- Library requests: GET data dari JSONPlaceholder (https://jsonplaceholder.typicode.com)
- Lambda + higher-order function: map, filter, sorted
- Module json: menyimpan hasil analisis ke hasil_analisis.json

Jalankan:  pip install -r ../../requirements.txt  (atau: pip install requests)
           python analisis_api.py
"""

import json
import os
from collections import Counter

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def ambil_data(endpoint):
    """GET satu endpoint JSONPlaceholder, return list/dict JSON."""
    response = requests.get(f"{BASE_URL}/{endpoint}", timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    print("=== Soal 5: Analisis API JSONPlaceholder ===")
    print(f"Mengambil data dari {BASE_URL}/posts dan /users ...")
    posts = ambil_data("posts")
    users = ambil_data("users")
    print(f"Berhasil: {len(posts)} posts, {len(users)} users")

    nama_user = {u["id"]: u["name"] for u in users}

    # map + lambda: panjang judul setiap post
    panjang_judul = list(map(lambda p: len(p["title"]), posts))
    rata_panjang_judul = sum(panjang_judul) / len(panjang_judul)

    # filter + lambda: post dengan judul panjang (> 60 karakter) dan (> 40)
    judul_panjang = list(filter(lambda p: len(p["title"]) > 60, posts))
    # filter: post milik userId 1
    posts_user1 = list(filter(lambda p: p["userId"] == 1, posts))

    # sorted + lambda: 5 post dengan judul terpanjang
    top5_terpanjang = sorted(posts, key=lambda p: len(p["title"]), reverse=True)[:5]

    # sorted + lambda: jumlah post per user, terbanyak dulu
    hitung_per_user = Counter(map(lambda p: p["userId"], posts))
    per_user_sorted = sorted(hitung_per_user.items(), key=lambda kv: kv[1], reverse=True)
    posts_per_user = [
        {"userId": uid, "nama": nama_user.get(uid, "-"), "jumlah_post": jumlah}
        for uid, jumlah in per_user_sorted
    ]

    # map + lambda: ringkasan post (id, judul singkat, penulis)
    ringkasan = list(
        map(
            lambda p: {
                "id": p["id"],
                "judul": p["title"][:50],
                "penulis": nama_user.get(p["userId"], "-"),
            },
            posts[:10],
        )
    )

    hasil = {
        "sumber": f"{BASE_URL}/posts",
        "total_post": len(posts),
        "total_user": len(users),
        "rata_rata_panjang_judul_karakter": round(rata_panjang_judul, 2),
        "judul_terpanjang_karakter": max(panjang_judul),
        "judul_terpendek_karakter": min(panjang_judul),
        "jumlah_post_judul_di_atas_60_karakter": len(judul_panjang),
        "jumlah_post_user_id_1": len(posts_user1),
        "top_5_judul_terpanjang": [
            {
                "id": p["id"],
                "judul": p["title"],
                "panjang": len(p["title"]),
                "penulis": nama_user.get(p["userId"], "-"),
            }
            for p in top5_terpanjang
        ],
        "post_per_user": posts_per_user,
        "ringkasan_10_post_pertama": ringkasan,
    }

    print(f"\nTotal post                 : {hasil['total_post']}")
    print(f"Rata-rata panjang judul    : {hasil['rata_rata_panjang_judul_karakter']} karakter")
    print(f"Judul terpanjang/terpendek : {hasil['judul_terpanjang_karakter']} / {hasil['judul_terpendek_karakter']} karakter")
    print(f"Post judul > 60 karakter   : {hasil['jumlah_post_judul_di_atas_60_karakter']}")
    print(f"Post milik userId 1        : {hasil['jumlah_post_user_id_1']}")

    print("\nTop 5 judul terpanjang:")
    for p in hasil["top_5_judul_terpanjang"]:
        print(f"  [{p['panjang']:>3} karakter] {p['judul']} — {p['penulis']}")

    print("\nPost per user (sorted terbanyak):")
    for item in posts_per_user:
        print(f"  {item['nama']:<22}: {item['jumlah_post']} post")

    # Simpan hasil ke file JSON memakai module json
    path_hasil = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hasil_analisis.json")
    with open(path_hasil, "w", encoding="utf-8") as f:
        json.dump(hasil, f, indent=2, ensure_ascii=False)
    print("\nHasil disimpan ke: hasil_analisis.json")
    return hasil


if __name__ == "__main__":
    main()
