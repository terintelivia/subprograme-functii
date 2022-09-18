x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
w=int(input("w:"))
def suma(a,b,c,d):
    s=(((a*d)+(c*b))/(b*d))
    return s
print("suma fractiilor=" ,suma(x,y,z,w))
def produs(a,b,c,d):
    p=((a*c)/(b*d))
    return p
print("produsul fractiilor=" ,produs(x,y,z,w))
