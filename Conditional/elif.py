age=int(input("Enter your age:"))
amount=float(input("Enter Bill amount:"))
if age<10:
    discountamt=amount*(50/100)
    finalamt=amount-discountamt
    print(f"fees discount is 50% and your final bill is {finalamt:.2f}")
elif(age>=10 and age<15):
    discountamt=amount*(25/100)
    finalamt=amount-discountamt
    print(f"fees discount is 25% and your final bill is {finalamt:.2f}")
elif(age>=15 and age<20):
    discountamt=amount*(10/100)
    finalamt=amount-discountamt
    print(f"fees discount is 10% and your final bill is {finalamt:.2f}")
elif(age>=20 and age<25):
    print(f"No discount and your final bill is {amount:.2f}")
else:
    print("Kamala Ja")
