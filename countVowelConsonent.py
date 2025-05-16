a=input("Enter the string: ")
vowels=0
consonents=0
for i in a:
    if i!=" ":
        if i in "aeiouAEIOU":
            vowels+=1
        else:
            consonents+=1
print("Number of vowels:",vowels)
print("Number of consonents:",consonents)