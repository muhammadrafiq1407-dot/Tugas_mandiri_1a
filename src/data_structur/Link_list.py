
from typing import Any


class Node:
    """
    Merepresentasikan satu elemen dalam singly linked list.

    Attributes:
        data: Data yang disimpan dalam node.
        next: Referensi menuju node berikutnya.
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


class LinkedList:
    """
    Mengelola kumpulan data mahasiswa menggunakan singly linked list.

    Operasi:
    - tambah: Menambahkan mahasiswa di akhir list.
    - hapus_by_nim: Menghapus mahasiswa berdasarkan NIM.
    - cari_by_nim: Mencari mahasiswa berdasarkan NIM.
    - tampilkan: Mengambil seluruh data mahasiswa.
    - jumlah: Menghitung jumlah node.
    - kosong: Memeriksa apakah list kosong.
    - bersihkan: Menghapus seluruh node.
    """

    def __init__(self) -> None:
        """Menginisialisasi linked list kosong."""
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def tambah(self, data: Any) -> None:
        """
        Menambahkan mahasiswa ke akhir linked list.

        Kompleksitas waktu: O(1).
        """
        if data is None:
            raise ValueError("Data mahasiswa tidak boleh None.")

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def hapus_by_nim(self, nim: str) -> bool:
        """
        Menghapus mahasiswa berdasarkan NIM.

        Returns:
            True jika data berhasil dihapus.
            False jika NIM tidak ditemukan.

        Kompleksitas waktu:
            Best case: O(1).
            Worst case: O(n).
        """
        current = self.head
        previous = None

        while current is not None:
            if current.data.nim == nim:

                # Jika node yang dihapus berada di awal.
                if previous is None:
                    self.head = current.next

                # Jika node berada di tengah atau akhir.
                else:
                    previous.next = current.next

                # Perbarui tail jika node terakhir dihapus.
                if current is self.tail:
                    self.tail = previous

                self._size -= 1

                # Putuskan referensi node yang dihapus.
                current.next = None

                return True

            previous = current
            current = current.next

        return False

    def cari_by_nim(self, nim: str) -> Any | None:
        """
        Mencari mahasiswa berdasarkan NIM.

        Returns:
            Objek mahasiswa jika ditemukan, None jika tidak.
        """
        current = self.head

        while current is not None:
            if current.data.nim == nim:
                return current.data

            current = current.next

        return None

    def tampilkan(self) -> list[Any]:
        """Mengembalikan seluruh data mahasiswa dalam bentuk list."""
        hasil = []
        current = self.head

        while current is not None:
            hasil.append(current.data)
            current = current.next

        return hasil

    def jumlah(self) -> int:
        """Mengembalikan jumlah node dalam linked list."""
        return self._size

    def kosong(self) -> bool:
        """Memeriksa apakah linked list kosong."""
        return self.head is None

    def bersihkan(self) -> None:
        """Menghapus seluruh node dari linked list."""
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None
            current = next_node

        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        """Memungkinkan penggunaan len() pada objek linked list."""
        return self._size

    def __iter__(self):
        """Memungkinkan linked list digunakan dalam perulangan."""
        current = self.head

        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Menghasilkan representasi linked list yang mudah dibaca."""
        return " -> ".join(str(data) for data in self)