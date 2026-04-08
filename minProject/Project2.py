menu={
    "Samosa":20,
    "coffee":20
}
 
print("------Menu--------")
for key,value in menu.items(): 
    print(key,value)
samosa=int(input("Enter Quantity of samosa:"))
coffee=int(input("Enter Quantity of Coffee:"))
total=(samosa*menu["Samosa"])+(coffee*menu["coffee"])

print("------Bill-------")
print(f"samosa {samosa}={samosa*menu['Samosa']}")
print(f"coffee {coffee}={coffee*menu['coffee']}")

print(f"total Amount={total}")