
def max(a,b):
    m=0
    if a>b:
       m=a
    if b>a:
       m=b
    return m 
def min(a,b):
    mi=0
    if a<b:
       mi=a
    if b<a:
       mi=b
    return mi


def nrmaxmin(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    S=max(min(a1,a2),max(a3,a4))+min(max(a5,a6),min(a7,a8))
    T=min(a1,a2)+min(a3,a4)+min(a5,a6)+min(a7,a8)+min(a9,a10)+max(a1,a2)+max(a3,a4)+max(a5,a6)+max(a7,a8)+max(a9,a10)
    return print("Valorea primei expresii:",S,"Valorea la a doua expresie:",T)

k1=int(input("Dati primul numar:"))
k2=int(input("Dati al doilea numar:"))
k3=int(input("Dati al treilea numar:"))
k4=int(input("Dati al patrulea numar:"))
k5=int(input("Dati al cincilea numar:"))
k6=int(input("Dati al saselea numar:"))
k7=int(input("Dati al saptelea numar:"))
k8=int(input("Dati al optlea numar:"))
k9=int(input("Dati al noualea numar:"))
k10=int(input("Dati al zecelea numar:"))
nrmaxmin(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10)
