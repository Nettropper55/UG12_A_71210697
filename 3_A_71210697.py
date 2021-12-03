kata=str(input("input:"))
print("Output :")
s = 0
for i in kata:
    s = s+1
    print(kata[0:s])

for i in kata:
    s = s-1
    print(kata[0:s])
