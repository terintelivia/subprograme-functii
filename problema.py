a=int(input("Dati primul numar:"))
b=int(input("Dati al doilea numar:"))
c=int(input("Dati al treilea numar:"))
def cmmdivizorcomun(z):
    cmmdc=[]
    for i in range (1,z+1):
        if (a*b==0):
            a+b
    else:
        while(a!=b):
            if(a>b): 
                a=a-b
        else:
            b=b-a
    return 0
print("Cel mai mare divizor comun:",cmmdivizorcomun(a,b,c))
def numarmaxim(a,b,c):
    if (a>b and a>c):
        print(a,"cel mai mare numar")
    if (c>a and c>b):
        print(c,"cel mai mare numar")
    if (b>c and b>a):
        print(b,"cel mai mare numar") 
def numarminim(a,b,c):
    if (a<b and a<c):
        print(a,"cel mai mic numar")
    if (c<a and c<b):
        print(c,"cel mai mic numar")
    if (b<c and b<a):
        print(b,"cel mai mic numar")