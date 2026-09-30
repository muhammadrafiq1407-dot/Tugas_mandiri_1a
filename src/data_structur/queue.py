from collections import deque


class Queue:
    """
    Struktur data Queue dengan prinsip FIFO
    (First In, First Out).

    Elemen yang pertama masuk akan menjadi
    elemen pertama yang diproses.
    """

    def __init__(self):
        # deque digunakan sebagai tempat penyimpanan data
        self.items = deque()

    # ==================================================
    # MENAMBAHKAN DATA
    # ==================================================

    def enqueue(self, item):
        """
        Menambahkan item ke bagian belakang antrean.

        Kompleksitas: O(1)
        """
        if item is None:
            raise ValueError("Item tidak boleh None")

        self.items.append(item)

    # ==================================================
    # MENGAMBIL DATA
    # ==================================================

    def dequeue(self):
        """
        Mengambil dan menghapus item paling depan.

        Kompleksitas: O(1)

        Mengembalikan None jika antrean kosong.
        """
        if not self.is_empty():
            return self.items.popleft()

        return None

    # ==================================================
    # MELIHAT DATA PALING DEPAN
    # ==================================================

    def peek(self):
        """
        Melihat item paling depan tanpa menghapusnya.

        Kompleksitas: O(1)
        """
        if not self.is_empty():
            return self.items[0]

        return None

    # ==================================================
    # MEMERIKSA ANTREAN KOSONG
    # ==================================================

    def is_empty(self):
        """
        Mengecek apakah antrean kosong.

        Kompleksitas: O(1)
        """
        return len(self.items) == 0

    # ==================================================
    # MENGHITUNG JUMLAH ITEM
    # ==================================================

    def size(self):
        """
        Mengembalikan jumlah item dalam antrean.

        Kompleksitas: O(1)
        """
        return len(self.items)

    # ==================================================
    # MENGAMBIL SEMUA DATA
    # ==================================================

    def get_all(self):
        """
        Mengembalikan seluruh isi antrean
        tanpa mengubah antrean asli.

        Kompleksitas: O(n)
        """
        return list(self.items)

    # ==================================================
    # MENGHAPUS SEMUA DATA
    # ==================================================

    def clear(self):
        """
        Menghapus seluruh isi antrean.

        Kompleksitas: O(n)
        """
        self.items.clear()

    # ==================================================
    # SPECIAL METHODS
    # ==================================================

    def __len__(self):
        """Mengembalikan jumlah item dalam Queue."""
        return len(self.items)

    def __str__(self):
        """Menampilkan isi Queue."""
        return str(list(self.items))

