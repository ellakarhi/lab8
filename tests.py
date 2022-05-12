count = 0
student = []
students = []
name = ""
grade = 0

while name != 'exit':
 
  name = input("Enter a name:")
  
  if name != 'exit':
    student.append(name)
    grade = int(input("Enter grade: "))
    student.append(grade)

    students.append(student)
    student = []

print (student)