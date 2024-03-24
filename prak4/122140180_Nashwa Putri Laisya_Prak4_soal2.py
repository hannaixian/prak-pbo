import math

class Persegi():
    def __init__(self, sisi):
        self.sisi = sisi
    def hitungLuas(self):
        return self.sisi * self.sisi
    
class Lingkaran():
    def __init__(self, radius):
        self.radius = radius
    def hitungLuas(self):
        return math.pi * self.radius**2
    
# def func(obj):
#     obj.hitungLuas()
    
persegi = Persegi(5)
lingkaran = Lingkaran(3)

# func(persegi)
# func(lingkaran)

print(f"Luas Persegi: {persegi.hitungLuas()}")
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}")