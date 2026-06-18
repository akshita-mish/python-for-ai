#super is used to call a parent class method from a child class 
class Employee:
    def __init__(self):
        print("I am employee class constructor ")

class Programmer(Employee):
    def __init__(self):
        super().__init__() #I am employee class constructor  (it will giev this)
        print("I am programmer class constructor")

p=Programmer()

