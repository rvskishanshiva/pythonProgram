a=input("select the operation you want to perform: +,-,*,/")
b=int(input("Enter the first number: "))    
c=int(input("Enter the second number: "))
if a=="+":
    print(b+c)
elif a=="-":
    print(b-c)  
elif a=="*":
    print(b*c)
else:
    print(b/c)