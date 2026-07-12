
you=input("enter your choice:")
choices={
    "s":-1,
    "w":1,
    "g":0
}
your=choices[you]
print(f"your choice is :{choices[you]}")
# import random

# computer=random.choice([-1,1,0]),if we want to play with computer
computerstar=input("enter the value:")
computer_choices={
    "s":-1,  #-1:"s"
    "w":1,   #1:"w",if we want to play with computer
    "g":0    #0:"g"
    
}
computer=computer_choices[computerstar]

print(f"the chioce of computer: {computer_choices[computerstar]}")

if(computer==-1 and your==1):
    print("computer win")
elif(computer==-1 and your==0):
    print("you win")
elif(computer==1 and your==-1):
    print("you win")
elif(computer==1 and your==0):
    print("computer win")
elif(computer==0 and your==-1):
    print("computer win")
elif(computer==0 and your==1):
     print("you win")
elif(computer==your):
    print("it is draw")
else:
    print("thier is somthing wrong")

