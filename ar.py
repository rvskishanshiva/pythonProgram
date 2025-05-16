def array_dig_mul(list):
    list2=[]
    for i in list:
        b=1
        while i!=0:
            a = i % 10 if i >= 0 else -(abs(i) % 10)
            b=b*a
            i=int(abs(i/10))
        list2.append(b)
    return list2

a=[-13,11,16,63,76,45,99]

result=array_dig_mul(a)
print(result)