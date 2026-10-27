"""Formatter tampilan data mahasiswa."""


def format_mahasiswa(mahasiswa):
    return (
        f"[{mahasiswa.nim}] {mahasiswa.nama} | {mahasiswa.jurusan} | "
        f"IPK {mahasiswa.ipk:.2f} | {mahasiswa.status}"
    )


def format_tabel(daftar_mahasiswa):
    baris = ["Daftar Mahasiswa:", "-" * 60]
    baris += [format_mahasiswa(m) for m in daftar_mahasiswa]
    baris.append("-" * 60)
    baris.append(f"Total: {len(daftar_mahasiswa)} mahasiswa")
    return "\n".join(baris)


if __name__ == "__main__":
    print(format_mahasiswa.__doc__)
