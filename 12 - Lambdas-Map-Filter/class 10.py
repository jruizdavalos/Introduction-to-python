students=[
    {"name":"Alice","age":18,"grade":"A"},
    {"name": "Bob", "age": 17, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"},
    {"name": "David", "age": 16, "grade": "C"},
    {"name": "Eve", "age": 17, "grade": "A"}
]

students_filter= list(filter(lambda s: s["grade"]=="A" and s["age"]>=18,students))

print(students_filter)