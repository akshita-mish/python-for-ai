# file handling in python 
#  first we ned to select a file and we need to open it up 
import os
print("directory : ",os.getcwd())
print("files in directory : ",os.listdir())
f=open("file.txt") # here we can also add mode like open("file.txt","mode") by defualt it is r
data=f.read()
print(data)
f.close()
