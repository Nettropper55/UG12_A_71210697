deret = input("Masukan deret angka :")
deret = deret.split(",")
x = 0
jenis = ""
Total = ""
for angka in deret:
    if angka != ",":
      if ((int(angka))%2) ==0:
        x = x + int(angka)
        jenis = " + "+angka
      else:
        x = x - int(angka)
        jenis = " - "+angka
      Total = Total + jenis

print("Total :",Total)
print("Hasil perhitungan diatas ialah",x)