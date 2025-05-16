list = [8,3,5,1,9,2]
# revlist=[]
# for i in range(len(list)-1,-1,-1):
#     revlist.append(list[i])
# print(revlist)

l=0
r=len(list)-1
while(l < r):
    list[l], list[r]=list[r], list[l]
    l+=1
    r-=1

print(list)