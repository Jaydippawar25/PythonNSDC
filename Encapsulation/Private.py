class Bank:
    def __init__(self):
        self.__bal = 10000

    def show_bal(self):
        print("Balance:",self.__bal)

b = Bank()
b.show_bal()

# print(b.__bal)  # Error 
#print(b._Bank__bal)