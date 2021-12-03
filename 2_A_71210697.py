x = str(input("Masukkan nama: "))
#nomor = nomer kursi
nomor = []
#bimo = daftar nama
nama = []
while x != "STOP":
    g = "Masukkan nomor kursi "+x+" : "
    y    =input(g)
    if y not in nomor:
        nomor.append(y)
        nama.append(x)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    x = str(input("Masukkan nama: "))
print("List kursi yang telah terisi :")
for i in range (len(nomor)):
    print("Kursi nomor %s telah diisi oleh %s"%(nomor[i], nama[i]))
