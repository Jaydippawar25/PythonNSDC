PIN=1234
count=3

 
while count>0:
    n=int(input("Enter a pin:"))
    count-=1
    if n==PIN:
        print("Access Granted")
        break
    elif n!=PIN and count!=0:
        print(f"Re-enter the pin. remaining attempt {count} ")
    else:
        print("your card is block")
 