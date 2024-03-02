jari2 = int(input("Masukkan jari-jari :"))
phi = 3.14

if(jari2 < 0):
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    keliling = phi * jari2 * 2
    Luas = phi * jari2 * jari2
    print("Keliling lingkaran = " + str(keliling))
    print("Luas lingkaran = " + str(luas))
