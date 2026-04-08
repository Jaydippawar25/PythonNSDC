from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Paid Using UPI")
class Card(Payment):
    def pay(self):
        print("Paid using Card")

p1= UPI()
p2 = Card()
p1.pay()
p2.pay()