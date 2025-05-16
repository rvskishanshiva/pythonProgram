a=input("Enter the character: ")
for b in a:
    if b.isalpha():
        if b in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            print(b, "is a vowel")
        else:
            print(b, "is a consonent")
    else:
        print(b, " is not a letter.")
