
from typing import Any


class ArrayMahasiswa:
    """
    Mengelola data mahasiswa menggunakan struktur data array.

    Operasi yang tersedia:
    - Menambahkan data mahasiswa.
    - Menghapus data mahasiswa berdasarkan indeks.
    - Menghapus data mahasiswa terakhir.
    - Mencari data mahasiswa.
    - Mengakses data berdasarkan indeks.
    - Menampilkan seluruh data mahasiswa.
    """

    def __init__(self) -> None:
        """Menginisialisasi array kosong."""
        self._data: list[Any] = []

    def tambah(self, mahasiswa: Any) -> None:
        """
        Menambahkan mahasiswa ke akhir array.

        Args:
            mahasiswa: Data mahasiswa yang akan ditambahkan.
        """
        if mahasiswa is None:
            raise ValueError("Data mahasiswa tidak boleh kosong.")

        self._data.append(mahasiswa)

    def hapus_terakhir(self) -> Any | None:
        """
        Menghapus dan mengembalikan elemen terakhir.

        Returns:
            Data mahasiswa yang dihapus atau None jika array kosong.
        """
        if not self._data:
            return None

        return self._data.pop()

    def hapus(self, indeks: int) -> Any:
        """
        Menghapus mahasiswa berdasarkan indeks.

        Args:
            indeks: Posisi mahasiswa dalam array.

        Returns:
            Data mahasiswa yang berhasil dihapus.

        Raises:
            IndexError: Jika indeks tidak valid.
        """
        if not 0 <= indeks < len(self._data):
            raise IndexError("Indeks mahasiswa tidak valid.")

        return self._data.pop(indeks)

    def cari(self, mahasiswa: Any) -> int:
        """
        Mencari posisi mahasiswa dalam array.

        Returns:
            Indeks mahasiswa jika ditemukan, -1 jika tidak ditemukan.
        """
        try:
            return self._data.index(mahasiswa)
        except ValueError:
            return -1

    def ambil(self, indeks: int) -> Any:
        """
        Mengakses mahasiswa berdasarkan indeks.

        Raises:
            IndexError: Jika indeks tidak valid.
        """
        return self._data[indeks]

    def tampilkan(self) -> list[Any]:
        """Mengembalikan salinan seluruh data mahasiswa."""
        return self._data.copy()

    def jumlah(self) -> int:
        """Mengembalikan jumlah mahasiswa dalam array."""
        return len(self._data)

    def kosong(self) -> bool:
        """Memeriksa apakah array kosong."""
        return len(self._data) == 0

    def bersihkan(self) -> None:
        """Menghapus seluruh data mahasiswa."""
        self._data.clear()

    def __len__(self) -> int:
        """Memungkinkan penggunaan len() pada objek array."""
        return len(self._data)

    def __str__(self) -> str:
        """Menghasilkan representasi array yang mudah dibaca."""
        return str(self._data)