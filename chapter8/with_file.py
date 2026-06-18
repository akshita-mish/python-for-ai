# f=open("text.file")
# data=f.read()
# f.close()
# this can be written as in simplest way , like we do not need to close the file explicitly

with open("file.txt") as f:
    print(f.read())