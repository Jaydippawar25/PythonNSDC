menu={
    "coffee":20,
    "Samosa":20,
     
}
 
print("------Menu--------")
for key,value in menu.items():
    
    print(key,value)
choice = int(input("Enter no item : "))
qty = int(input("Enter Quantity"))

Bill={

}
 
key=list(menu.keys())
value=list(menu.values())
total=0
count=0
Bill[key[choice-1]]=value[choice-1]
print("------Bill-------")
print("Sr. Item  Price  Qunatity")

for key,value in Bill.items():
    count+=1
    print(count,".",key," ",value," ",qty)
    total+=value*qty
print("TotalBill:",total)