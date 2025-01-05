class ClassData:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_data(self, nama, nilai):
        self.data_mahasiswa.append({"nama": nama, "nilai": nilai})

    def get_data(self):
        return self.data_mahasiswa


class ClassView:
    @staticmethod
    def tampilkan_data(data):
        if not data:
            print("Tidak ada data untuk ditampilkan.")
            return
        print(f"{'No.':<5} {'Nama':<20} {'Nilai':<10}")
        print("=" * 40)
        for i, item in enumerate(data, 1):
            print(f"{i:<5} {item['nama']:<20} {item['nilai']:<10}")


class ClassProcess:
    def __init__(self, data_obj):
        self.data_obj = data_obj

    def input_data(self):
        while True:
            try:
                nama = input("Masukkan nama mahasiswa: ").strip()
                if not nama:
                    raise ValueError("Nama tidak boleh kosong!")
                
                nilai = input("Masukkan nilai mahasiswa: ").strip()
                if not nilai.isdigit() or not (0 <= int(nilai) <= 100):
                    raise ValueError("Nilai harus berupa angka antara 0-100!")
                
                self.data_obj.tambah_data(nama, int(nilai))

                lanjut = input("Apakah ingin menambahkan data lagi? (y/n): ").strip().lower()
                if lanjut != 'y':
                    break
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Kesalahan tak terduga: {e}")


# Main program
if __name__ == "__main__":
    data = ClassData()
    proses = ClassProcess(data)
    view = ClassView()

    proses.input_data()
    view.tampilkan_data(data.get_data())