class Cal:
    def add(self, a=None,b=None):
        if a is not None and b is not None:
            print("Sum of two nums:",a+b)
        elif a is not None:
            print("Single value:",a)
        else:
            print("No values")

c = Cal()
c.add(5,3)
c.add(5)
c.add()