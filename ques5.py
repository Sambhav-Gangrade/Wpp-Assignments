students = []
for i in range(10):
    name = input(f"Enter the name of student {i+1}: ")[:5]
    students.append(name)
for name in students:
    print(name[::-1])