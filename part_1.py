#Ini adalah komen
#kita bisa menggunakan tanda pagar untuk menulis komen di python
'''
ini  komen dengan multi line,
kita bisa menulis apa saja di dalamnya
dengan menggunakan tanda kutip tiga
dan tidak akan di eksekusi oleh komputer
'''
#ini adalah print
#print berfungsi menampilkan teks/angka/nilai di layar (output)
#untk string kita harus menggunakan tanda kutip
print("Hallo Python")
print("Selamat Datang Di Pemograman Python............... \
      sambungan....\
      ")
#print untuk angka tidak perlu tanda kutip
print(1)

#print untuk variable kita bisa langsung mengetikan nama variable nya tanpa kutip
nama = "ofan"
angka = 17
print(nama)
print(angka)

#menggabungkan teks dan variable di print kita bisa menggunakan cara :
#1. dengan meggunakan koma
print("hallo",nama,"Nomor Kamu adalah :", angka)
#2. dengan string interpolasi (f-string)
print(f"hallo {nama},Nomor Kamu adalah :, {angka}")
#3. dengan metode .format()
print("halo {}, Nomor Anda adalah : {}".format(nama,angka))

#kita juga bisa menggunakan print untuk menampilkan hasil perhitungan mtk
print(1+2)

#newline
print("diatas adalah contoh contoh\n dasar pemograman python")

#menampilkan teks tanpa baris baru
print("baris ke satu", end="")
print("baris kedua")
