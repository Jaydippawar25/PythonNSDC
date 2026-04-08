class Payment:
    def pay(self):
        print("General Payment")

class UPI(Payment):
    def pay(self):
        print("Payment Using Upi")

class card(Payment):
    def pay(self):
        print("Payment Using Card")

p1 = UPI()
p2 = card()

p1.pay()
p2.pay()