#it means to create a new list from an existing  sequence of elements 
# it is a very cleaner way to do it 

print("new list")
# new list =[expression for item in iterable ]

#expression = which you want to add in new list(besically the operation)
#item= new variable
#iterable= the ds on which you are applying operation 


# suppose we have to do the square of numbers and then we need to add it into the new list 
#  the older way would be 
square=[]
for i in range(1,11):
    square.append(i*i)
print(square)

new_sqr=[i*i for i in range(1,11)]
print(new_sqr)  #more efficient

# comprehension with condition
new_sqr1=[i*i for i in range(1,11) if i%2!=0]
print(new_sqr1)

# another way to do it 
num=[1,2,3,4,5,6,7,8,9,10]
even_num=[i for i in num if i%2==0]
print(even_num)

# another way
label=["Even" if x%2==0 else "Odd" for x in num]
print(label)

# with strings
names=["akshita","anjali","akshat","rahul","rohini"]
name_li = [name.startswith("a") for name in names]
print(name_li)

# if the code is long and complex so do not use list comprehension , 
# it can make the code messier in that particular  scenario