# Examples of Dictionary using input from Keyboard

number_of_students=int(input("Enter number of students:"))
student_dict={}
i=1
while i<=number_of_students:
    name=input("Enter Student name:")
    mark=input("Enter % of marks of Student:")
    student_dict[name]=mark
    i=i+1
print("Name of Student","\t","% of marks")
for percent_mark in student_dict:
    print("\t",percent_mark,"\t\t",student_dict[percent_mark])
