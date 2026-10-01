class Mahasiswa:
    def __init__(self, nama, nim, prodi, email, angkatan):
        # Atribut utama mahasiswa
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.email = email
        self.angkatan = angkatan

    def tampilkan_data(self):
        print("=== Data Mahasiswa ===")
        print(f"Nama      : {self.nama}")
        print(f"NIM       : {self.nim}")
        print(f"Prodi     : {self.prodi}")
        print(f"Email     : {self.email}")
        print(f"Angkatan  : {self.angkatan}")

    def ubah_email(self, email_baru):
        if not email_baru:
            raise ValueError("Email baru tidak boleh kosong")

        self.email = email_baru

    def ubah_prodi(self, prodi_baru):
        if not prodi_baru:
            raise ValueError("Prodi baru tidak boleh kosong")

        self.prodi = prodi_baru

    def identitas(self):
        return f"{self.nama} ({self.nim})"

    def __repr__(self):
        return (
            f"Mahasiswa("
            f"Nama: '{self.nama}', "
            f"NIM: '{self.nim}', "
            f"Prodi: '{self.prodi}', "
            f"Email: '{self.email}', "
            f"Angkatan: {self.angkatan}"
            f")"
        )
