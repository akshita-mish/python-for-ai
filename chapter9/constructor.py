class Student:
    name="Akshita" # this is a class attribute 
    lang="English"
    def __init__(self):
        print("Creating a student object") #dunder method called automatically
    def getName(self): # always use self in function in python inside a class
        print(f"This student is {self.name} and she speaks {self.lang} very well ")
    @staticmethod #this is used when you do not take any object property
    def greet():
        print("Hello akshita ")

stu=Student()
stu.name="Anshika" #this is an instance attribute 
# instance attribute has higher precendece over class attributes 
print(stu.name)
stu.getName()
stu.greet()