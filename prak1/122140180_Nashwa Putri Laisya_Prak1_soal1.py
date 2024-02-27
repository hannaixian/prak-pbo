lower = int (input ("Batas bawah : "))
upper = int (input ("Batas atas : "))

sum = 0

if lower < 0 or upper < 0:
    print ("Batas bawah dan atas yang dimasukkan tidak boleh di bawah nol!")
else:
    for i in range (lower, upper):
        if i % 2 == 0:
            pass
        else:
            sum += i
            print (i)
    print ("Total : " + str(sum))