import random
number=random.randint(1,5)
att=3
while att>0:
    num=int(input("Guess the number between 1 to 5:"))
    att-=1
    if number==num:
        print("You win")
        break
    elif number!=num and att!=0:
        print(f"Better luck try again...Remaining attmepts are {att}")
    else:
        print(f"All attmepts are over Game is Finshed...Correct number is:{number}")
