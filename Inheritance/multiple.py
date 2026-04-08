class Father :
    def Skill1(self):
        print("Driving")

class mother :
    def Skill2(self):
        print("Cooking")

class Child(Father, mother) :
    def Skill3(self):
        print("Codeing")

c = Child()
c.Skill1()
c.Skill2()
c.Skill3()