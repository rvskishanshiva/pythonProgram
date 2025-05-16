list =[5,2,8,4,3]
max=list[0]
min=list[0]
for i in list:
    if max<i:
        max=i
    if min>i:
        min=i    
print(min)
print(max)            