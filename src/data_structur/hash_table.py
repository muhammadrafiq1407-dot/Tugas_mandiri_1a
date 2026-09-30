class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        """Menambahkan atau memperbarui data berdasarkan key."""
        if key is None:
            raise ValueError("Key tidak boleh None")

        self.table[key] = value

    def search(self, key):
        """Mencari data berdasarkan key."""
        return self.table.get(key, None)

    def delete(self, key):
        """Menghapus data berdasarkan key."""
        if key in self.table:
            del self.table[key]
            return True

        return False

    def contains(self, key):
        """Mengecek apakah key tersedia."""
        return key in self.table

    def get_all(self):
        """Mengambil seluruh data."""
        return self.table.copy()

    def size(self):
        """Mengembalikan jumlah data."""
        return len(self.table)

    def is_empty(self):
        """Mengecek apakah Hash Table kosong."""
        return len(self.table) == 0

    def clear(self):
        """Menghapus seluruh data."""
        self.table.clear()

    def __len__(self):
        return len(self.table)

    def __contains__(self, key):
        return key in self.table

    def __str__(self):
        return str(self.table)