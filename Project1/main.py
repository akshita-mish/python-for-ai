# we are making a snake , water , gun game 
#  here we have 1 for snake , -1 for water , and 0 for gun 
import random
computer= random.choice([-1,0,1])
choice=input("enter you choice : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[choice]

print(f"Computer choice : {reverseDict[computer]} \n Your choice : {reverseDict[you]}")
if(computer == you):
    print("Game draw !!")
else:
    if(computer==1 and  you ==0):
        print("You won")
    elif(computer==1 and you == -1):
        print("computer won")
    elif(computer == -1 and you ==0):
        print("Comouter won ")
    elif(computer ==-1 and you ==1):
        print("you won")
    elif(computer==0 and you == 1):
        print("computer won")
    elif(computer==0 and you ==-1):
        print("you won")
    else:
        print("something went wrong ")

        

