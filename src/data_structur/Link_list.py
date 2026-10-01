
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def tambah(self, data: Any) -> None:
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
        current = self.head

        while current is not None:
            if current.data.nim == nim:
                return current.data

            current = current.next

        return None

    def tampilkan(self) -> list[Any]:
        hasil = []
        current = self.head

        while current is not None:
            hasil.append(current.data)
            current = current.next

        return hasil

    def jumlah(self) -> int:
        return self._size

    def kosong(self) -> bool:
        return self.head is None

    def bersihkan(self) -> None:
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None
            current = next_node

        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return " -> ".join(str(data) for data in self)