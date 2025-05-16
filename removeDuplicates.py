l = [1, 3, 7, 2, 2, 3, 9, 4, 8, 3, 9, 1, 5, 2, 8, 3, 7, 1]
i = 0

while i < len(l): 
    j = i + 1
    while j < len(l):
        if l[i] == l[j]:
            del l[j]
            j+=1
        else:
            j += 1
    i += 1
# for i in range(0,len(l)-1,1):
#     for j in range(i+1,len(l)-1,1):
#         if l[i]==l[j]:
#             del l[j]

print(l)
