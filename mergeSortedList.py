list1=[2,3,5,7,9]
list2=[5,8,11,12]
i,j=0,0
mergeList=[]
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        mergeList.append(list1[i])
        i+=1
    elif list2[j]<list1[i]:
        mergeList.append(list2[j])
        j+=1
    else:
        mergeList.append(list2[j])
        j+=1
        i+=1
       
while i<len(list1):
    mergeList.append(list1[i])
    i+=1
while j<len(list2):
    mergeList.append(list2[j])
    j+=1

print(mergeList)               
