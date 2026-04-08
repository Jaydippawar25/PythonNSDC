class gp:
    def land(self):
        print("land")
class Parent(gp):
    def show(self):
        print("Parent class...")

class child(Parent):
    def display(self):
        print("Child class...")

c= child()
c.land()
c.show()
c.display()