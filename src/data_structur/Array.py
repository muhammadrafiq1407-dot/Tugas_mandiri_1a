
from typing import Any


class ArrayMahasiswa:
    def __init__(self) -> None:
        self._data: list[Any] = []

    def tambah(self, mahasiswa: Any) -> None:
        if mahasiswa is None:
            raise ValueError("Data mahasiswa tidak boleh kosong.")

        self._data.append(mahasiswa)

    def hapus_terakhir(self) -> Any | None:
        if not self._data:
            return None

        return self._data.pop()

    def hapus(self, indeks: int) -> Any:
        if not 0 <= indeks < len(self._data):
            raise IndexError("Indeks mahasiswa tidak valid.")

        return self._data.pop(indeks)

    def cari(self, mahasiswa: Any) -> int:
        try:
            return self._data.index(mahasiswa)
        except ValueError:
            return -1

    def ambil(self, indeks: int) -> Any:
        return self._data[indeks]

    def tampilkan(self) -> list[Any]:
        return self._data.copy()

    def jumlah(self) -> int:
        return len(self._data)

    def kosong(self) -> bool:
        return len(self._data) == 0

    def bersihkan(self) -> None:
        self._data.clear()

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return str(self._data)