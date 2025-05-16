s1={1,2,3,4,5}
s2={4,2,7,1,9}
l1=list(s1)
l2=list(s2)
intSec=[]
for i in l1:
    for j in l2:
        if i==j:
            intSec.append(i)
intSec=set(intSec)
print(intSec)