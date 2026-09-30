
from typing import Any


class Stack:
    """
    Mengimplementasikan struktur data Stack dengan prinsip LIFO.

    LIFO (Last In, First Out):
    Elemen yang terakhir dimasukkan akan menjadi elemen
    pertama yang dikeluarkan.

    Digunakan untuk mendukung fitur Undo pada sistem akademik.
    """

    def __init__(self) -> None:
        """Menginisialisasi stack kosong."""
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """
        Menambahkan elemen ke bagian atas stack.

        Args:
            item: Data atau aksi yang akan disimpan.

        Kompleksitas: O(1) amortized.
        """
        if item is None:
            raise ValueError("Item tidak boleh None.")

        self._items.append(item)

    def pop(self) -> Any | None:
        """
        Mengambil dan menghapus elemen paling atas.

        Returns:
            Elemen terakhir jika stack tidak kosong.
            None jika stack kosong.

        Kompleksitas: O(1).
        """
        if self.is_empty():
            return None

        return self._items.pop()

    def peek(self) -> Any | None:
        """
        Melihat elemen paling atas tanpa menghapusnya.

        Returns:
            Elemen teratas atau None jika stack kosong.

        Kompleksitas: O(1).
        """
        if self.is_empty():
            return None

        return self._items[-1]

    def is_empty(self) -> bool:
        """Memeriksa apakah stack kosong."""
        return len(self._items) == 0

    def size(self) -> int:
        """Mengembalikan jumlah elemen dalam stack."""
        return len(self._items)

    def clear(self) -> None:
        """Menghapus seluruh elemen dalam stack."""
        self._items.clear()

    def get_all(self) -> list[Any]:
        """Mengembalikan salinan seluruh elemen stack."""
        return self._items.copy()

    def __len__(self) -> int:
        """Memungkinkan penggunaan len() pada objek stack."""
        return len(self._items)

    def __str__(self) -> str:
        """Menampilkan isi stack dengan format yang mudah dibaca."""
        return str(self._items)