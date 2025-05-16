a=int(input("Enter a number to check if it is an Armstrong number: "))
b=a
sum=0
d=a
count=0
while(d>0):
    d=d//10
    count=count+1
while a>0:
    c=a%10
    sum=sum+c**count
    a=a//10
if b==sum:
    print(b," is an Armstrong number.")
else:
    print(b," is not an Armstrong number.")
