n=int(input())
m=int(input())
def factorial(x):
    fact=1
    for i in range(1,x+1):
       fact=fact*i
    return fact
c=(factorial(n)/(factorial(m)*factorial(n-m)))
print(c)