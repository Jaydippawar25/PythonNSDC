class Bank:
    def __init__(self):
        self.__bal =1000

    def get_bal(self):
        return self.__bal
    def set_bal(self,amount):
        if amount >= 0:
            self.__bal += amount
        else:
            print("Invalid amount")

b = Bank()
print("Initial Balance:",b.get_bal())
b.set_bal(1500)
print("Update Balance:",b.get_bal())
b.set_bal(-500)