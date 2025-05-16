def flatten(nested):
    flat = []  
    for i in range(len(nested)):
        if type(nested[i]) == list:  
            flat += flatten(nested[i])
        else:
            flat += [nested[i]]  
    return flat


nested = [1, [2, [3, 4],[7,99,13,75,24], 5], [6, 7], 8]
print(flatten(nested))  



# nested = [1, [2, [3, 4],[7,99,13,75,24], 5], [6, 7], 8]
# list=sum(nested,[])
# print(list)