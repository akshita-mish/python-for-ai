class Animal:
    name="Lion"
    color="gold"
    def makesound(self):
        print(f"the {self.name} makes sound ")

#child class
class Dog(Animal):
    name="dog"
    color="black"
    def sayColor(self):
        print(f"the dog has a color {self.color}")
    

d=Dog()
d.makesound()
d.sayColor()
