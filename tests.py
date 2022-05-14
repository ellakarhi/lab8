student_grades = []
student = []
students = []
def get_students():
  student = []
  students = []
  name = ""
  grade = 0
  while True:
    name = input("Enter a name: ")

    if name == "exit":
      break

    student.append(name)
    grade = int(input("Enter grade: "))
    student.append(grade)
    student.append(student)
    student = []
  return students

def get_average(students):
  total = 0
  for student in students:
    total  += student[1]
    
  average = total / len(students)
  return average 

def highest_grade(students):
  student.sort(key=lambda x:x[1])
  print (students)

student_grades = [["Alice", 99] ["Bob", 98] ["Charlie", 98]]

average = round(get_average(student_grades),2)
print(f"The class average is (average)")
highest_grade(student_grades)


#all_students = get_students()



#print (student)