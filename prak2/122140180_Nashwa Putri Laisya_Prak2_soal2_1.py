def punya_kucing (func):
    def wrapper (*args):
        print ("Saya punya kucing dengan ciri-ciri sebagai berikut.")
        func(*args)
    return wrapper

class Cat:

    def __init__(self, ras, umur):
        self.ras = ras
        self.umur = umur

    @punya_kucing
    def ciri_kucing (self):
        print (f"Ras : {self.ras} \nUmur : {self.umur}")

    def __del__ (self):
        print ("Data kucing dihapus.")

kucing1 = Cat("Mainecoon", "5 bulan")
kucing1.ciri_kucing()