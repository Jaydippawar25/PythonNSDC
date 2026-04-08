menu={
    "1":"check bal",
    "2":"deposite",
    "3":"Withdraw",
    "4":"Exit"


}
print("------Menu--------")
for key,value in menu.items():
    print(key,value)
choice=input("Enter your choice:")
class bank:
    def __init__(self,bal):
         
        self.__bal=bal
    def Check_bal(self):
         print(f"bal:{self.__bal}")

    def deposit(self):
        amount=float(input("Enter a amount"))
        if amount>0:
            self.__bal+=amount
            print(f"Deposited Successfully  ")
        else:
            print("Invalid deposit amount")
    def Withdraw(self):
         amount=float(input("Enter a amount"))
         if amount<0:
             print("Invaid Withdraw amount")
         elif amount> self.__bal:
             print("Insufficient balance")            
         else:
            self.__bal -= amount
            print(f"Withdrawal Successfull {amount} ")
bal = bank(3000)
while(1):
    if choice=="1":
        bal.Check_bal()
        break
    elif choice=='2':
        bal.deposit()
        bal.Check_bal()
        break
    elif choice=="3":
        bal.Withdraw()
        bal.Check_bal()
        break
    elif choice=='4':
        print("Thank you")
        break
else:
        print("Invalid choice")

