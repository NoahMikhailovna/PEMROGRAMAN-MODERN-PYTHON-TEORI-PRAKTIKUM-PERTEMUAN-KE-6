"""Model Mahasiswa (sistem_informasi.model.mahasiswa)."""

from dataclasses import dataclass


@dataclass
class Mahasiswa:
    """Entitas mahasiswa."""

    nim: str
    nama: str
    jurusan: str = "Sistem Informasi"
    ipk: float = 0.0
    status: str = "Aktif"

    def to_dict(self):
        return {
            "nim": self.nim,
            "nama": self.nama,
            "jurusan": self.jurusan,
            "ipk": self.ipk,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nim=data["nim"],
            nama=data["nama"],
            jurusan=data.get("jurusan", "Sistem Informasi"),
            ipk=data.get("ipk", 0.0),
            status=data.get("status", "Aktif"),
        )

    def __str__(self):
        return f"{self.nim} - {self.nama} ({self.jurusan}, IPK {self.ipk:.2f}, {self.status})"


if __name__ == "__main__":
    m = Mahasiswa("20241320038", "Fakhry Ahmad Fauzan", ipk=3.75)
    print(m)
    print(m.to_dict())
    print(Mahasiswa.from_dict(m.to_dict()))
