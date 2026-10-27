"""Package sistem_informasi — CRUD Mahasiswa in-memory.

Subpackage:
- model   : definisi entitas Mahasiswa
- service : logika CRUD Mahasiswa
- utils   : validasi & formatter
"""

__version__ = "1.0.0"
__all__ = ["model", "service", "utils"]

from .model.mahasiswa import Mahasiswa  # noqa: F401 - diekspos agar mudah diimpor
from .service.mahasiswa_service import MahasiswaService  # noqa: F401
