class Employee:
    a=1
    @classmethod #it helps to call the class atrribute but we need to use cls here  
    def fun(cls):
        print(f"the value of class attribute a is {cls.a}")       

e=Employee()
e.a=67
e.fun() # we will get 1 as an output 