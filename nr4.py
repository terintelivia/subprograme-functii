from random import randint
suma=0
while True:
    numar1=randint(1,6)
    numar2=randint(1,6)
    suma=numar1+numar2
    if (numar1==numar2):
        print("Dubla este:",numar1)
        break
print("Suma dublei este:",suma)