student_grades = []

def get_students():
  student = []
  students = []
  name = ""
  grade = 0
  
  while True:
    name = input("Enter a name: ")
    grade = int(input("Enter grade: "))
    if name == 'exit':
      break
        
    student.append(name)
    student.append(grade)
    students.append(student)
    student = []
  
    return students


def get_average(students):
  """Gets the average of student's grades."""
  total = 0 
  for student in students:
    total += student[1]

  average = total / len(students)  
  return average

def highest_grade(students):
  """Gives highest grade"""
  students.sort(key=lambda x:x[1])
  print (students)
  
#student_grades = [['Alice', 99], ['Bob', 98], ['Charlie', 98]]
student_grades = get_students()
average = round(get_average(student_grades),2)
print (f"The class average is {average}")
highest_grade(student_grades)
