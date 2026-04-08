add=0
odd=0
for i in range(1,101):
    if i%2==0:
        add+=i
    else:
        odd+=i
print(f"Addtion of 1 to 100 even numbers is {add}")
print(f"Addtion of 1 to 100 odd numbers is {odd}")