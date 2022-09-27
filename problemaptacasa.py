x = int(input("introduceti numarul "))
y = int(input("introduceti numarul "))
z = int(input("introduceti numarul "))
def numarmax(a,b,c):
    m=0
    if (a>b and a>c):
        m=a
    if (c>a and c>b):
        m=c
    if (b>c and b>a):
        m=b
    return m
print("Cel mai mare numar:",numarmax(x,y,z)) 
def numarmin(a,b,c):
    min=0
    if (a<b and a<c):
        min=a
    if (c<a and c<b):
        min=c
    if (b<c and b<a):
        min=b
    return min
print("Cel mai mic numar:",numarmin(x,y,z)) 
def cmmdiv(a,b,c):
    cmmdiv=0
    divisor= numarmax(a,b,c)
    while(divisor>1):
        if(a%divisor==0 and b%divisor==0 and c%divisor==0):
            cmmdiv=divisor
            break
        divisor-=1
    return cmmdiv
print("Cel mai mare divizor comun al numerelor: ",cmmdiv(x,y,z))
def cmultipl(a,b,c):
    cmultipl=0
    divisor=numarmax(a,b,c)
    while True:
        if(divisor%a==0) and (divisor%b==0) and (divisor%c==0):
            cmultipl=divisor
            break
        divisor+=1
    return cmultipl
print("Cel mai mic multiplu comun al numerelor: ",cmultipl(x,y,z))
import math
def triunghi(a,b,c):
    if ( (a+b>c) and (a+c>b) and (b+c>a) ):
        perim=((a+b+c)/2)*2
        return perim
    else:
        return print("Laturile nu pot forma un triunghi")
print("Laturile date pot forma un triunghi,iar perimetrul este egal cu:",triunghi(x,y,z))
def aria(a,b,c):
    if ( (a+b>c) and (a+c>b) and (b+c>a) ):
        perimetru=a+b+c
        semip=perimetru/2
        aria=round(math.sqrt(semip*(semip-a)*(semip-b)*(semip-c)),2)
        return aria
    else:
        return print("Laturile nu pot forma un triunghi")
print("Laturile date pot forma un triunghi,iar aria este egala cu:",aria(x,y,z))
def divcomuni(a,b,c):
    l1=[]
    l2=[]
    l3=[]
    for i in range (1,a+1):
        if (a%i==0):
            l1.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            l2.append(j)
    for k in range (1,c+1):
        if (c%k==0):
            l3.append(k)
    dc=set(l1).intersection(l2)
    dc3=set(dc).intersection(l3)
    divizori=list(dc3)
    return divizori
print("Divizorii comuni ai numerelor: ",divcomuni(x,y,z))
def multiplicomuni(a,b,c):
    m=[]
    for i in range(1,4):
        m.append(abs(i*numarmax(a,b,c)))
    return m
print("3 multipli comuni ai numerelor:",multiplicomuni(x,y,z))
def ecuatia(a,b,c):
        delta=(b**2)-(4*a*c)
        if delta>0:
            s1=(-b-(math.sqrt(delta))/(2*a))
            s2=(-b+(math.sqrt(delta))/(2*a))
            return print("Ecuatia are solutii reale:",s1,s2)
        elif delta==0:
            s1=s2=(-b)/(2*a)
            return print("Ecuatia are solutii egale:",s1)
        else:
            return print("Ecuatia nu are solutii reale")
(ecuatia(x,y,z))
