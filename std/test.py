class car:
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def display(self):
        print("This car is a " +self.color+" "+self.model+".")
car1 = car("Toyota Corolla","Red")
car2 = car("Honda Civic","Blue")
print(car1.model)
print(car2.color)
car1.display()
car2.display()
        