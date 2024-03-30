people= [
    {'name':'Jon Doe', 'age': 30},
    {'name':'Jane Doe', 'age': 25},
    {'name':'Reber Go', 'age': 40},
]

f=sorted(people, key=lambda person: person['age'])
print(f)