
import random
computer=random.randint(1,3)

dict1={1:"Rock",2:"Paper", 3:"Scissor"}
print(" \nRock_Paper_Scissors GAME :-\n\t\t\n\t\t1: 'Rock' \n\t\t2: 'Paper'\n\t\t3: 'Scissor'")
choice=int(input("\nENTER YOUR CHOICE : "))

for i in range(1,5):
    for j in range(1,2):
        print("\t\t\t\t\t | ")
print(end="\t\t\t\t\t | ")

print(f"\n\t YOUR CHOICE :- {dict1[choice]}",f"\t\t\t COMPUTER CHOICE :- {dict1[computer]}")

for i in range(1,5):
    for j in range(1,2):
        print("\t\t\t\t\t | ")
print(end="")

print("\n\t\t\t",end="   ")
if choice==computer:
    print("******* ITS A DRAW *******")
elif choice==1 and computer==2:
    print("********* COMPUTER WON *********")
elif choice==1 and computer==3:
    print("********** YOU WON **********")
elif choice==2 and computer==1:
    print("********** YOU WON **********")
elif choice==2 and computer==3:
    print("******** COMPUTER WON ********")
elif choice==3 and computer==1:
    print("******** COMPUTER WON ********")
elif choice==3 and computer==2:
    print("********** YOU WON **********")
else:
    print("INVALID INPUT, TRY AGAIN ")

