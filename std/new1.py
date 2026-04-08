class Student:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
    def show(self):
        print("Name:",self.Name)
        print("Age:",self.Age)
s1=Student("ram",20)
s2=Student("mm",44)
print(s1.Name)
print(s2.Age)
s1.show()
s2.show()
