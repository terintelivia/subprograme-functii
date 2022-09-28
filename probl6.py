x=int(input("Dati primul numar:"))
y=int(input("Dati al doilea numar:"))
z=int(input("Dati al treilea numar:"))
w=int(input("Dati al patrulea numar:"))
import math
def triunghi(a,b,c,d):
    if ( (a+b>c) and (a+c>b) and (b+c>a) ):
        perim=(a+b+c)
        return print("Laturile", a,b,c, "pot forma un triunghi","Perimetrul este:",perim)
    elif ( (a+b>d) and(a+d>b) and b+d>a):
        perim=(a+b+d)
        return print("Laturile", a,b,d,"pot forma un triunghi","Perimetrul este:",perim) 
    elif ( (a+c>d) and (a+d>c) and (c+d>a)):
        perim=(a+c+d)
        return print("Laturile ",a,c,d, "pot forma un triunghi","Perimetrul este:",perim)
    elif ( (b+c>d) and (b+d>c) and (c+d>b)):
        perim=(b+c+d)
        return print("Laturile", b,c,d, "pot forma un triunghi","Perimetrul este:",perim)
    else:
        return print("Laturile nu pot forma un triunghi")
triunghi(x,y,z,w)
def aria(a,b,c,d):
    if ( (a+b>c) and (a+c>b) and (b+c>a) ):
       perimetru=(a+b+c)
       semip=perimetru/2
       aria=round(math.sqrt(semip*(semip-a)*(semip-b)*(semip-c)),2)
       return print("Aria formata de laturile",a,b,c,"este:",aria)
    elif ( (a+b>d) and(a+d>b) and b+d>a):
       perimetru=(a+b+d)
       semip=perimetru/2
       aria=round(math.sqrt(semip*(semip-a)*(semip-b)*(semip-d)),2)
       return print("Aria formata de laturile",a,b,d,"este:",aria) 
    elif ( (a+c>d) and (a+d>c) and (c+d>a)):
       perimetru=(a+c+d)
       semip=perimetru/2
       aria=round(math.sqrt(semip*(semip-a)*(semip-c)*(semip-d)),2)
       return print("Aria formata de laturile",a,c,d,"este:",aria) 
    elif ( (b+c>d) and (b+d>c) and (c+d>b)):
       perimetru=(b+c+d)
       semip=perimetru/2
       aria=round(math.sqrt(semip*(semip-b)*(semip-c)*(semip-d)),2)
       return print("Aria formata de laturile",b,c,d,"este:",aria)
    else:
        return print("Laturile nu pot forma un triunghi")  
aria(x,y,z,w)