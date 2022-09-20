nr1=int(input("Dati un numar:"))
nr2=int(input("Dati un alt numar:"))
def suma(x,y):
    return x+y
print("suma=" ,suma(nr1,nr2))
def produs(x,y):
    return x*y
print ("produsul=" , produs(nr1,nr2))
def mediaaritmetica(x,y):
    return (x+y)/2
print ("mediaaritmetica=" ,mediaaritmetica(nr1,nr2))
def cmmdivizorcomun(x,y):
    while x!=y:
        if x>y:x =x-y
        else:y=y-x
    return x
print('cmmdivizorcomun =', cmmdivizorcomun(nr1,nr2))
print('cmmmultimplucomun =', str(nr1*nr2 // cmmdivizorcomun(nr1,nr2)))
def nrminim(x,y):
    return min([x,y])
print ("nrminim=" ,nrminim(nr1,nr2))
def nrmaxim(x,y):
    return max([x,y])
print ("nrmaxim=" ,nrmaxim(nr1,nr2))
def sumanrcitite():
    a=int(input("Dati a:"))
    b=int(input("Dati b:"))
    return a+b
print("suma ab=" ,sumanrcitite())
def produsnrcitite():
    a=int(input("Dati a:"))
    b=int(input("Dati b:"))
    return a*b
print("produsul ab=" ,produsnrcitite())
def divizoricomuni(x,y):
    d=0
    for i in range(1,x+1):
        if x%i==0:
            d+=1
    return d
print("divizori comuni=", divizoricomuni(nr1,nr2))
def multiplicomuni(x,y):
    m=[]
    for i in range(1,6):
        m.append(abs(cmmdivizorcomun(x,y))*i)
    return m
print("5multiplicomuni=", multiplicomuni(nr1, nr2))
def cifrecomune(x,y):
    return list(set(str(x)).intersection(set(str(y))))
print("cifre comune=", cifrecomune(nr1,nr2))
def cifrediferite(x,y):
    return list(set(str(x)).difference(set(str(y))))
print("cifrele care se contin in primul numar,iar in al doilea nu=",cifrediferite(nr1,nr2))
def cifreprietene(x,y):
    if len([i for i in range(1,x+1) if x%i==0])==len([i for i in range(1,y+1) if y%i==0]):
        return 'PRIETENIE'
print("Prietene", cifreprietene(nr1,nr2)
