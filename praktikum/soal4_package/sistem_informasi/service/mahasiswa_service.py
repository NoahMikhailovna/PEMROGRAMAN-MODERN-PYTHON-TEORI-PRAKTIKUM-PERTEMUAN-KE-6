"""Service CRUD Mahasiswa dengan penyimpanan dictionary in-memory."""

from ..model.mahasiswa import Mahasiswa
from ..utils.validasi import validasi_mahasiswa


class MahasiswaService:
    """CRUD sederhana; data disimpan di dict {nim: Mahasiswa}."""

    def __init__(self):
        self._storage = {}

    # CREATE
    def tambah(self, mahasiswa):
        """Menambah mahasiswa baru. Return (bool, pesan)."""
        valid, errors = validasi_mahasiswa(mahasiswa)
        if not valid:
            return False, "; ".join(errors)
        if mahasiswa.nim in self._storage:
            return False, f"NIM {mahasiswa.nim} sudah terdaftar"
        self._storage[mahasiswa.nim] = mahasiswa
        return True, f"Mahasiswa {mahasiswa.nama} ditambahkan"

    # READ
    def ambil(self, nim):
        """Mengambil satu mahasiswa berdasarkan NIM, None bila tidak ada."""
        return self._storage.get(nim)

    def ambil_semua(self):
        """Mengambil semua mahasiswa, diurutkan berdasarkan NIM."""
        return [self._storage[nim] for nim in sorted(self._storage)]

    def cari(self, kata_kunci):
        """Mencari mahasiswa yang namanya mengandung kata kunci."""
        kata = kata_kunci.lower()
        return [m for m in self._storage.values() if kata in m.nama.lower()]

    # UPDATE
    def ubah(self, nim, **data_baru):
        """Mengubah field mahasiswa. Return (bool, pesan)."""
        mahasiswa = self._storage.get(nim)
        if mahasiswa is None:
            return False, f"NIM {nim} tidak ditemukan"
        for field in ("nama", "jurusan", "ipk", "status"):
            if field in data_baru:
                setattr(mahasiswa, field, data_baru[field])
        valid, errors = validasi_mahasiswa(mahasiswa)
        if not valid:
            return False, "; ".join(errors)
        return True, f"Data NIM {nim} diperbarui"

    # DELETE
    def hapus(self, nim):
        """Menghapus mahasiswa. Return (bool, pesan)."""
        if nim not in self._storage:
            return False, f"NIM {nim} tidak ditemukan"
        del self._storage[nim]
        return True, f"Data NIM {nim} dihapus"

    def jumlah(self):
        return len(self._storage)


if __name__ == "__main__":
    svc = MahasiswaService()
    print(svc.tambah(Mahasiswa("001", "Budi", ipk=3.5)))
    print(svc.ambil("001"))
