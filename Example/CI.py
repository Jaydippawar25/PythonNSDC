import math
p=float(input("Enter a principle:"))
r=float(input("Enter a time:"))
t=float(input("Enter a rate:"))

a=p*((1+(r/100))**t)
print(f"amount:{a:.2f}")
