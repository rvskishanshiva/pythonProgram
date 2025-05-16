a=int(input("Enter the number: "))
sum=0
while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10
print(sum)