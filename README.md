# Academic Data Structure & Complexity Analysis

**Implementasi Struktur Data dan Analisis Kompleksitas pada Sistem Akademik Menggunakan Python**

## Deskripsi

Proyek ini merupakan implementasi struktur data dalam studi kasus sistem akademik untuk mengelola data mahasiswa. Proyek dikembangkan sebagai bagian dari tugas mata kuliah Struktur Data dan Analisis Kompleksitas.

Implementasi mencakup penyimpanan data secara berurutan, pengelolaan data dinamis, mekanisme Undo, sistem antrean, serta pencarian data berdasarkan kunci tertentu.

## Struktur Data yang Digunakan

| Struktur Data | Implementasi        | Kegunaan                                |
| ------------- | ------------------- | --------------------------------------- |
| Array         | Python List         | Penyimpanan data berurutan              |
| Linked List   | Custom Node         | Penambahan dan penghapusan data dinamis |
| Stack         | Python List         | Mekanisme Undo (LIFO)                   |
| Queue         | `collections.deque` | Antrean pengolahan data (FIFO)          |
| Hash Table    | Python Dictionary   | Pencarian mahasiswa berdasarkan NIM     |

## Teknologi

- Python 3
- Git dan GitHub
- unittest

## Cara Menjalankan

1. Clone repository.
2. Masuk ke direktori proyek.
3. Jalankan program utama.

```bash
python src/main.py
```

## Pengujian

Jalankan pengujian dengan perintah:

```bash
python -m unittest discover -s tests -v
```

## Dokumentasi

Penjelasan konsep, hubungan algoritma dan struktur data, analisis kompleksitas, serta alasan pemilihan struktur data tersedia dalam direktori `docs/`.

## Presentasi

Materi presentasi dan tautan video dapat ditemukan dalam direktori `presentation/`.

## Author

Nama: [Nama Mahasiswa]
Program Studi: Teknik Informatika
Mata Kuliah: Struktur Data dan Analisis Kompleksitas
