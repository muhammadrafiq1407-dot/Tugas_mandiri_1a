
from typing import Any


class Stack:
    def __init__(self, max_capacity: int | None = None) -> None:
        self._items: list[Any] = []
        self._max_capacity: int | None = max_capacity

    def push(self, item: Any) -> None:
        if item is None:
            raise ValueError("Item tidak boleh None.")

        # Jika kapasitas penuh, buang riwayat aksi tertua (paling bawah di indeks 0)
        if self._max_capacity is not None and len(self._items) >= self._max_capacity:
            self._items.pop(0)

        self._items.append(item)

    def pop(self) -> Any | None:
        if self.is_empty():
            return None

        return self._items.pop()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None

        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def get_all(self) -> list[Any]:
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return str(self._items)