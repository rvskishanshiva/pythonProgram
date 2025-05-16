a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
print("The greatest common divisor of",a,"and",b,"is",gcd(a,b))