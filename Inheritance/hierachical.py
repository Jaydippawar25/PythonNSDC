class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def Bark(self):
        print("Bark")
class Cat(Animal):
    def meow(self):
        print("meow")

d = Dog()
c = Cat()

d.eat() 
c.eat()