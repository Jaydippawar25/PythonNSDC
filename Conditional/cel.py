choice=input("Select(C Or F):")
if choice =='c':

    cel=float(input("Enter the celcius:"))
    f=(cel*9/5)+32
    print("temp in f is",f)
elif(choice=='f'):
    f=float(input("Enter the farahnaght:"))
    cel=(f-32)*5/9
    print(f"temp in c is",cel)
else:
    print("Enter correct code...")