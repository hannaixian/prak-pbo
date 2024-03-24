class Hewan:
    def __init__(self, nama, jk):
        self.nama = nama
        self.jeniskelamin = jk

    def bersuara (self):
        pass

    def makan (self):
        pass

    def minum (self):
        pass

class Kucing (Hewan):
    def __init__(self, nama, jk):
        super().__init__(nama, jk)

    def bersuara(self):
        print (f"Kucing {self.nama} bersuara: Meong!")

    def makan(self):
        print (f"Kucing {self.nama} sedang makan: ikan")
    
    def minum(self):
        print (f"Kucing {self.nama} sedang minum: susu")
    

class Anjing (Hewan):
    def __init__(self, nama, jk):
        super().__init__(nama, jk)

    def bersuara(self):
        print (f"Anjing {self.nama} bersuara: Guk Guk!")

    def makan(self):
        print (f"Anjing {self.nama} sedang makan: tulang")
    
    def minum(self):
        print (f"Anjing {self.nama} sedang minum: air")
    
hewan1 = Kucing ("Kiki", "Betina")
hewan2 = Anjing ("Ichi", "Jantan")

print (hewan1.nama)
print (hewan2.nama)

hewan1.bersuara()
hewan1.makan()
hewan2.bersuara()
hewan2.minum()