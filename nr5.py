import random
m=int(input("Dati numarul de elemente:"))
l=[]
suma=0
for i in range(m):
    l.append(random.randint(1,100))
for i in l:
    if i!=max(l):
        suma+=i
print(l)
print("Suma elementelor este:",suma)