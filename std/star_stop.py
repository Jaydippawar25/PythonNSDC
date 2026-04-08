class car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    
    def start(self):
        print("The "+self.color+" "+self.brand+" "+self.model+" has started.")
    def stop(self):
         print("The "+self.color+" "+self.brand+" "+self.model+" has stop.")
car1=car("BMW","S7","white")
car2=car("Tata","Punch","black")
car1.start()
car1.stop()
car2.start()
car2.stop()    