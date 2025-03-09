#Assignment 5:
##Module 6: Data Structures and Strings in Python
###Author: Kapil Sharma
####Task1: Create a dictionary of Student Marks

student_marks = {'Ajay':90,'Alice':85,'Hemant':75,'Rahul':82,'Ram':98,'Shyam':90,'Uttam':81}
student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(student_name +"'s marks: ", student_marks.get(student_name))
else:
    print("Student not found.")