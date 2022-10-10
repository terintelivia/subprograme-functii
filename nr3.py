from random import randint
k=[]
for i in range(1):
    a=randint(0,999999999)
    print(a)
while a>0:
    r=a%10
    a//=10
    k.append(r)
print("0 apare de:",k.count(0),"ori")
print("1 apare de:",k.count(1),"ori")
print("2 apare de:",k.count(2),"ori")
print("3 apare de:",k.count(3),"ori")
print("4 apare de:",k.count(4),"ori")
print("5 apare de:",k.count(5),"ori")
print("6 apare de:",k.count(6),"ori")
print("7 apare de:",k.count(7),"ori")
print("8 apare de:",k.count(8),"ori")
print("9 apare de:",k.count(9),"ori")