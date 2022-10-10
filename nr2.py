from random import randint
m=int(input("Dati numarul de aruncari:"))
k=0
for x in range(m):
    a=randint(1,6)
    print(a)
    if a==6:
        k+=1
print("Valorea 6 a aparut de:",k,"ori")