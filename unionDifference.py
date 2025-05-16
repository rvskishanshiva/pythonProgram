a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = set()
difference_a_b = set()

for i in a:
    union.add(i)

for i in b:
    if i not in union:
        union.add(i)

for i in a:
    if i not in b:
        difference_a_b.add(i)


print("Union:", union)
print("Difference (B - A):", difference_a_b)