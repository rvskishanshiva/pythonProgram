import math
a=int(input("Enter the number: "))
if a>1:
    for i in range(2,round(math.sqrt(a))+1):
        if a%i==0:
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")