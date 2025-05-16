people = [
    {'name': 'Bob', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Charlie', 'age': 20}
]

people.sort(key=lambda x: x['age'])
print(people)

# sorted_people = sorted(people, key=lambda x: (x['age'], x['name']))
# print(sorted_people)