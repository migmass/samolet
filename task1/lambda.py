#лямбда сложение
func=lambda x, y: x+y
print(func(1,2))

print((lambda x,y:x+y)('a','y'))

student_tuples=[
    ('join', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sort_student=sorted(student_tuples, key=lambda student: student[2]) #сортировка по возрасту
 
print(sort_student)

