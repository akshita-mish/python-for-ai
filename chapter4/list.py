# a list in python is used to store any kind of data type 
# list are mutable means they can be modified 
fruits=["Orange","apple",675,78.9,"this is me"]
print(fruits[0])
fruits[0]="Mango"
print(fruits)

# append function in list ; add item at the end
fruits.append("Peach")
print(fruits)

# #sort 
# fruits.sort()
# print(fruits)  it will show error because list has diff types , so for sorting we need to make same type

li=["Apple","Mango","Orange","Grapes"]
# li.sort()
# print(li) #['Apple', 'Grapes', 'Mango', 'Orange']

li.reverse()
print(li)

#insert is used to add at a particular index
li.insert(0,"Banana");
print(li)

#pop will remove from the linex
val=li.pop(2);
print(val)
print(li)

# remove a particuler value
li.remove("Apple")
print(li)
