import random
m=int(input("Dati numarul de elemente:"))
Sumapoz=0
Sumaneg=0
for x in range(m):
    k=random.randint(-50,50)
    if k>0:
        Sumapoz=Sumapoz+k
    if k<0:
        Sumaneg=Sumaneg-k
print("Suma numerelor pozitive este:",Sumapoz)
print("Suma numerelor negative este:",Sumaneg)