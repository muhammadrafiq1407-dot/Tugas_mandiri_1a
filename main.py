import time
from datetime import datetime

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

        # Stack untuk fitur Undo (LIFO) dengan batas maksimum 6 kali
        self.history_undo = Stack(max_capacity=6)

        # Queue untuk antrean layanan (FIFO)
        self.antrean_layanan = Queue()


    def tambah_mahasiswa(
        self,
        nama,
        nim,
        prodi,
        email,
        angkatan
    ):
        t_start = time.perf_counter()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Pastikan NIM belum digunakan
        if self.index_nim.contains(nim):
            t_elapsed = (time.perf_counter() - t_start) * 1000
            print(
                f"[{waktu_sekarang}] [ERROR] Mahasiswa dengan NIM {nim} "
                f"sudah terdaftar. (Waktu: {t_elapsed:.4f} ms)"
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

        self.daftar_berurutan.tambah(mhs)
        self.daftar_dinamis.tambah(mhs)
        self.index_nim.insert(nim, mhs)
        self.history_undo.push(("TAMBAH", mhs))

        t_elapsed = (time.perf_counter() - t_start) * 1000
        print(
            f"[{waktu_sekarang}] [SUCCESS] Mahasiswa {nama} ({nim}) "
            f"berhasil ditambahkan. (Durasi: {t_elapsed:.4f} ms)"
        )

        return True


    def tampilkan_mahasiswa(self):
        """
        Menampilkan seluruh mahasiswa menggunakan Array.
        """
        t_start = time.perf_counter()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        print(f"\n=== DAFTAR MAHASISWA [{waktu_sekarang}] ===")

        data = self.daftar_berurutan.tampilkan()

        if not data:
            print("Belum ada data mahasiswa.")
            t_elapsed = (time.perf_counter() - t_start) * 1000
            print(f"(Durasi tampilkan: {t_elapsed:.4f} ms)")
            return

        for nomor, mhs in enumerate(data, start=1):
            print(
                f"{nomor}. "
                f"{mhs.nama} | "
                f"NIM: {mhs.nim} | "
                f"Prodi: {mhs.prodi} | "
                f"Angkatan: {mhs.angkatan}"
            )

        t_elapsed = (time.perf_counter() - t_start) * 1000
        print(f"(Durasi tampilkan: {t_elapsed:.4f} ms)")


    def cari_mahasiswa_by_nim(self, nim):
        """
        Mencari mahasiswa berdasarkan NIM menggunakan
        Hash Table.

        Average Case: O(1)
        """
        t_start = time.perf_counter()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        hasil = self.index_nim.search(nim)
        t_elapsed = (time.perf_counter() - t_start) * 1000

        if hasil:
            print(
                f"[{waktu_sekarang}] [CARI FOUND] NIM {nim} -> "
                f"{hasil.nama} (Pencarian Hash Table: {t_elapsed:.4f} ms)"
            )
        else:
            print(
                f"[{waktu_sekarang}] [CARI NOT FOUND] Mahasiswa dengan "
                f"NIM {nim} tidak ditemukan. (Pencarian Hash Table: {t_elapsed:.4f} ms)"
            )

        return hasil


    def undo(self):
        t_start = time.perf_counter()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        aksi_terakhir = self.history_undo.pop()

        if not aksi_terakhir:
            t_elapsed = (time.perf_counter() - t_start) * 1000
            print(
                f"[{waktu_sekarang}] [UNDO FAILED] Tidak ada riwayat "
                f"aksi untuk di-undo. (Waktu: {t_elapsed:.4f} ms)"
            )
            return False

        jenis_aksi, mhs = aksi_terakhir

        if jenis_aksi == "TAMBAH":
            # Hapus dari Array
            self.daftar_berurutan.hapus_terakhir()

            # Hapus dari Linked List berdasarkan NIM
            self.daftar_dinamis.hapus_by_nim(mhs.nim)

            # Hapus dari Hash Table berdasarkan NIM
            self.index_nim.delete(mhs.nim)

            t_elapsed = (time.perf_counter() - t_start) * 1000
            print(
                f"[{waktu_sekarang}] [UNDO SUCCESS] Membatalkan penambahan "
                f"mahasiswa: {mhs.nama} ({mhs.nim}) (Durasi LIFO Undo: {t_elapsed:.4f} ms)"
            )

            return True

        t_elapsed = (time.perf_counter() - t_start) * 1000
        print(
            f"[{waktu_sekarang}] [UNDO FAILED] Jenis aksi '{jenis_aksi}' "
            f"belum didukung. (Waktu: {t_elapsed:.4f} ms)"
        )
        return False

    def tambah_antrean_layanan(self, nim, jenis_layanan):
        t_start = time.perf_counter()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Cari mahasiswa terlebih dahulu melalui Hash Table
        mhs = self.index_nim.search(nim)

        if not mhs:
            t_elapsed = (time.perf_counter() - t_start) * 1000
            print(
                f"[{waktu_sekarang}] [ANTREAN ERROR] NIM {nim} "
                f"tidak terdaftar. (Waktu: {t_elapsed:.4f} ms)"
            )
            return False

        # Masukkan mahasiswa ke Queue
        self.antrean_layanan.enqueue(
            (mhs, jenis_layanan)
        )

        t_elapsed = (time.perf_counter() - t_start) * 1000
        print(
            f"[{waktu_sekarang}] [ANTREAN FIFO] {mhs.nama} masuk antrean "
            f"untuk: {jenis_layanan} (Durasi enqueue: {t_elapsed:.4f} ms)"
        )

        return True

    def proses_antrean_layanan(self):
        t_start = time.perf_counter()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        item = self.antrean_layanan.dequeue()

        if not item:
            t_elapsed = (time.perf_counter() - t_start) * 1000
            print(
                f"[{waktu_sekarang}] [PROSES LAYANAN] Antrean kosong. (Waktu: {t_elapsed:.4f} ms)"
            )
            return None

        mhs, jenis_layanan = item
        t_elapsed = (time.perf_counter() - t_start) * 1000

        print(
            f"[{waktu_sekarang}] [PROSES LAYANAN FIFO] Memproses "
            f"{jenis_layanan} untuk {mhs.nama} ({mhs.nim}) (Durasi dequeue: {t_elapsed:.4f} ms)"
        )

        return item



if __name__ == "__main__":

    # Membuat objek sistem akademik
    app = Sismik("Fakultas Ilmu Komputer")

    print("=" * 60)
    print("        SISTEM INFORMASI AKADEMIK")
    print(f"        {app.fakultas}")
    print("=" * 60)

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

    print("\n=== 2. PENCARIAN BERDASARKAN KEY ===")

    app.cari_mahasiswa_by_nim("2026002")

    app.cari_mahasiswa_by_nim("2026099")


    print("\n=== 3. FITUR UNDO (STACK - LIFO) ===")

    print("\nAksi terakhir adalah penambahan Eko.")
    print("Melakukan UNDO...")

    app.undo()

    print("\nMemeriksa kembali NIM 2026003:")

    app.cari_mahasiswa_by_nim("2026003")

    print("\nDaftar mahasiswa setelah UNDO:")
    app.tampilkan_mahasiswa()


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
    app.proses_antrean_layanan()

    app.proses_antrean_layanan()

    app.proses_antrean_layanan()

    print("\n" + "=" * 60)
    print("             PROGRAM SELESAI")
    print("=" * 60)

