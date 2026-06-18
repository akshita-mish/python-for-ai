# //find a program to find greatest using function
def greatest():
    n1=int(input("enter number 1: "))
    n2=int(input("enter number 2: "))
    n3=int(input("enter number 3: "))
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3
    
val=greatest()
print(f" {val} is greatest")

# do avoid new line to print in print() use end at the end of it like print(,end=" ")