from src.data_structur.Array import ArrayMahasiswa
from src.data_structur.Link_list import LinkedList
from src.data_structur.hash_table import HashTable
from src.data_structur.stack import Stack
from src.data_structur.queue import Queue

from src.aplication.sistem_akademik import Mahasiswa


class Sismik:
    def __init__(self, fakultas):
        self.fakultas = fakultas
        self.daftar_berurutan = ArrayMahasiswa()
        self.daftar_dinamis = LinkedList()

        # Hash Table untuk pencarian mahasiswa berdasarkan NIM
        self.index_nim = HashTable()

        # Stack untuk fitur Undo (LIFO)
        self.history_undo = Stack()

        # Queue untuk antrean layanan (FIFO)
        self.antrean_layanan = Queue()

    # ==================================================
    # 1. MENAMBAHKAN MAHASISWA
    # ==================================================

    def tambah_mahasiswa(
        self,
        nama,
        nim,
        prodi,
        email,
        angkatan
    ):
        """
        Menambahkan mahasiswa ke dalam sistem.

        Data mahasiswa disimpan ke:
        - Array
        - Linked List
        - Hash Table

        Aksi penambahan dicatat ke Stack untuk Undo.
        """

        # Pastikan NIM belum digunakan
        if self.index_nim.contains(nim):
            print(
                f"[ERROR] Mahasiswa dengan NIM {nim} "
                f"sudah terdaftar."
            )
            return False

        # Membuat objek Mahasiswa
        mhs = Mahasiswa(
            nama=nama,
            nim=nim,
            prodi=prodi,
            email=email,
            angkatan=angkatan
        )

        # ----------------------------------------------
        # Simpan ke Array
        # ----------------------------------------------
        self.daftar_berurutan.tambah(mhs)

        # ----------------------------------------------
        # Simpan ke Linked List
        # ----------------------------------------------
        self.daftar_dinamis.tambah(mhs)

        # ----------------------------------------------
        # Simpan ke Hash Table
        # NIM digunakan sebagai KEY
        # ----------------------------------------------
        self.index_nim.insert(nim, mhs)

        # ----------------------------------------------
        # Simpan histori ke Stack
        # Stack menggunakan prinsip LIFO
        # ----------------------------------------------
        self.history_undo.push(("TAMBAH", mhs))

        print(
            f"[SUCCESS] Mahasiswa {nama} ({nim}) "
            f"berhasil ditambahkan."
        )

        return True

    # ==================================================
    # 2. MENAMPILKAN SELURUH MAHASISWA
    # ==================================================

    def tampilkan_mahasiswa(self):
        """
        Menampilkan seluruh mahasiswa menggunakan Array.
        """

        print("\n=== DAFTAR MAHASISWA ===")

        data = self.daftar_berurutan.tampilkan()

        if not data:
            print("Belum ada data mahasiswa.")
            return

        for nomor, mhs in enumerate(data, start=1):
            print(
                f"{nomor}. "
                f"{mhs.nama} | "
                f"NIM: {mhs.nim} | "
                f"Prodi: {mhs.prodi} | "
                f"Angkatan: {mhs.angkatan}"
            )

    # ==================================================
    # 3. PENCARIAN MAHASISWA BERDASARKAN NIM
    # ==================================================

    def cari_mahasiswa_by_nim(self, nim):
        """
        Mencari mahasiswa berdasarkan NIM menggunakan
        Hash Table.

        Average Case: O(1)
        """

        hasil = self.index_nim.search(nim)

        if hasil:
            print(
                f"[CARI FOUND] NIM {nim} -> "
                f"{hasil.nama}"
            )
        else:
            print(
                f"[CARI NOT FOUND] Mahasiswa dengan "
                f"NIM {nim} tidak ditemukan."
            )

        return hasil

    # ==================================================
    # 4. FITUR UNDO
    # ==================================================

    def undo(self):
        """
        Membatalkan aksi terakhir menggunakan Stack.

        Stack menggunakan prinsip:
        LIFO (Last In, First Out)
        """

        aksi_terakhir = self.history_undo.pop()

        if not aksi_terakhir:
            print(
                "[UNDO FAILED] Tidak ada riwayat "
                "aksi untuk di-undo."
            )
            return False

        jenis_aksi, mhs = aksi_terakhir

        # ----------------------------------------------
        # Jika aksi terakhir adalah TAMBAH
        # ----------------------------------------------
        if jenis_aksi == "TAMBAH":

            # Hapus dari Array
            self.daftar_berurutan.hapus_terakhir()

            # Hapus dari Linked List berdasarkan NIM
            self.daftar_dinamis.hapus_by_nim(mhs.nim)

            # Hapus dari Hash Table berdasarkan NIM
            self.index_nim.delete(mhs.nim)

            print(
                f"[UNDO SUCCESS] Membatalkan penambahan "
                f"mahasiswa: {mhs.nama} ({mhs.nim})"
            )

            return True

        print(
            f"[UNDO FAILED] Jenis aksi '{jenis_aksi}' "
            f"belum didukung."
        )

        return False

    # ==================================================
    # 5. MENAMBAHKAN ANTREAN LAYANAN
    # ==================================================

    def tambah_antrean_layanan(self, nim, jenis_layanan):
        """
        Menambahkan mahasiswa ke antrean layanan.

        Queue menggunakan prinsip:
        FIFO (First In, First Out)
        """

        # Cari mahasiswa terlebih dahulu melalui Hash Table
        mhs = self.index_nim.search(nim)

        if not mhs:
            print(
                f"[ANTREAN ERROR] NIM {nim} "
                f"tidak terdaftar."
            )
            return False

        # Masukkan mahasiswa ke Queue
        self.antrean_layanan.enqueue(
            (mhs, jenis_layanan)
        )

        print(
            f"[ANTREAN] {mhs.nama} masuk antrean "
            f"untuk: {jenis_layanan}"
        )

        return True

    # ==================================================
    # 6. MEMPROSES ANTREAN
    # ==================================================

    def proses_antrean_layanan(self):
        """
        Memproses mahasiswa paling depan dalam antrean.

        Queue menggunakan prinsip FIFO.
        """

        item = self.antrean_layanan.dequeue()

        if not item:
            print(
                "[PROSES LAYANAN] Antrean kosong."
            )
            return None

        mhs, jenis_layanan = item

        print(
            f"[PROSES LAYANAN] Memproses "
            f"{jenis_layanan} untuk "
            f"{mhs.nama} ({mhs.nim})"
        )

        return item


# ==========================================================
# UJI COBA PROGRAM
# ==========================================================

if __name__ == "__main__":

    # Membuat objek sistem akademik
    app = Sismik("Fakultas Ilmu Komputer")

    print("=" * 60)
    print("        SISTEM INFORMASI AKADEMIK")
    print(f"        {app.fakultas}")
    print("=" * 60)

    # ======================================================
    # 1. PENYIMPANAN DATA BERURUTAN
    #    Menggunakan ARRAY
    # ======================================================

    print("\n=== 1. PENAMBAHAN DATA MAHASISWA ===")

    app.tambah_mahasiswa(
        "Budi Santoso",
        "2026001",
        "Teknik Informatika",
        "budi@gmail.com",
        2026
    )

    app.tambah_mahasiswa(
        "Siti Aminah",
        "2026002",
        "Teknik Informatika",
        "siti@gmail.com",
        2026
    )

    app.tambah_mahasiswa(
        "Eko Prasetyo",
        "2026003",
        "Sistem Informasi",
        "eko@gmail.com",
        2026
    )

    app.tampilkan_mahasiswa()

    # ======================================================
    # 2. PENCARIAN BERDASARKAN KEY
    #    Menggunakan HASH TABLE
    # ======================================================

    print("\n=== 2. PENCARIAN BERDASARKAN KEY ===")

    # NIM digunakan sebagai KEY
    app.cari_mahasiswa_by_nim("2026002")

    # NIM yang tidak ada
    app.cari_mahasiswa_by_nim("2026099")

    # ======================================================
    # 3. FITUR UNDO
    #    Menggunakan STACK (LIFO)
    # ======================================================

    print("\n=== 3. FITUR UNDO (STACK - LIFO) ===")

    print("\nAksi terakhir adalah penambahan Eko.")
    print("Melakukan UNDO...")

    app.undo()

    print("\nMemeriksa kembali NIM 2026003:")

    app.cari_mahasiswa_by_nim("2026003")

    print("\nDaftar mahasiswa setelah UNDO:")
    app.tampilkan_mahasiswa()

    # ======================================================
    # 4. ANTREAN PENGOLAHAN DATA
    #    Menggunakan QUEUE (FIFO)
    # ======================================================

    print("\n=== 4. ANTREAN LAYANAN (QUEUE - FIFO) ===")

    app.tambah_antrean_layanan(
        "2026001",
        "Cetak Transkrip"
    )

    app.tambah_antrean_layanan(
        "2026002",
        "Legalisir Ijazah"
    )

    print("\nMemproses antrean:")

    # Budi masuk lebih dahulu,
    # maka Budi diproses lebih dahulu
    app.proses_antrean_layanan()

    # Siti diproses setelah Budi
    app.proses_antrean_layanan()

    # Antrean sudah kosong
    app.proses_antrean_layanan()

    print("\n" + "=" * 60)
    print("             PROGRAM SELESAI")
    print("=" * 60)

