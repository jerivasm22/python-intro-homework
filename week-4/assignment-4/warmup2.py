
student = {
    "name" : "Stella", 
    "grade" : "A", 
    "subjects" : ["Math", "Science", "Spanish"]}
for key, value in student.items():
    print(f"{key}:{value}")
student["graduated"] = False
print(student)