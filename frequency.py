from collections import Counter
text = "hello world"
# freq = {} 
# for char in text:
#         if char ==" ":
#             continue
#         else:
#             # if char in freq:
#             #     freq[char] += 1  
#             # else:
#             #     freq[char] = 1 
#             # 2 freq[char]=freq.get(char,0)+1    



# print(freq)
# print(freq['h'])

print(Counter(text))