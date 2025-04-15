students = {'Mike':45, 'Nike':52, 'Jesus':67, 'Alice': 34}
name = input("Enter the student's name: ")  
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")