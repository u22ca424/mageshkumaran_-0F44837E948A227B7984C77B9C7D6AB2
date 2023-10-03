
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  # sort the list of students in decending order of CPGA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa, 
                           reverse=True)

  # Syntax - lambda arg:exp
  return sorted_students

#Example Usage:
students = [
    Student("Hariharan","u22ca401", 7.8),
    Student("Bala", "u22ca402", 8.9),
    Student("Gokul", "u22ca403", 9.1),
    Student("Magesh", "u22ca404", 9.9),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))