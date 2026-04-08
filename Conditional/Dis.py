amount=float(input("Enter old amount:"))
increment_per=float(input("Enter increment hike %:"))
hike=amount*(increment_per/100)
newamt=amount+hike
discount=float(input("Enter a product discount % : "))
discountamt=newamt*(discount/100)
finalamt=newamt-discountamt
print(f"Final price of Product {finalamt:.2f}")
 