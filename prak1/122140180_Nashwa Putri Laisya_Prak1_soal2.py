phi = 3.14

r = int (input ("Jari-jari : "))

keliling = 2 * phi * r
luas = phi * r * r

if r < 0 :
    print ("Jari-jari lingkaran tidak boleh negatif")
else:
    print ("Luas : " + str(luas))
    print ("Keliling : " + str(keliling))