class Mahasiswa:

    def __init__(self, nim, nama, angkatan, isMahasiswa = True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa
    
    def method1 (self):
        return f"Nama Mahasiswa/i : {self.__nama} \nNIM : {self.__nim}"
    def method2 (self):
        return f"Mahasiswa/i {self.__nama} dengan NIM {self.__nim} merupakan mahasiswa/i Angkatan {self.angkatan}"
    def method3 (self):
        return f"{self.__nama} {' merupakan seorang mahasiswa/i ITERA' if self.isMahasiswa else ' bukan mahasiswa/i ITERA'}"

    def get_nim (self):
        return self.__nim
    def set_nim (self, nim):
        self.__nim = nim
    def get_nama (self):
        return self.__nama
    def set_nama (self, nama):
        self.__nama = nama

mhs1 = Mahasiswa (122140180, "Nashwa Putri Laisya", 2022, True)

mhs2 = Mahasiswa (122210062, "Basil Caropeboka", 2022)

print (mhs1.method1())
print (mhs1.method2())
print (mhs1.method3())
print ("\n")
print (mhs2.method1())
print (mhs2.method2())
print (mhs2.method3())