class Student:
    name="Akshita" # this is a class attribute 
    lang="English"

stu=Student()
stu.name="Anshika" #this is an instance attribute 
# instance attribute has higher precendece over class attributes 
print(stu.name)