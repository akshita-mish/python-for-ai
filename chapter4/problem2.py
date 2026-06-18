student=[]
i=0;
while i<7:
    marks=int(input("enter marks : "))
    student.append(marks)
    i=i+1
student.sort()
print(student)