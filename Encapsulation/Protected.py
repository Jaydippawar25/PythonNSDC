class student:
    def __init__(self):
        self.name="Ram"
        self.__marks = 85

class Result(student):
    def show(self):
        # print("Name is",self.name)
        # print("Marks are",self._marks)
        pass

r = Result()
r.show()
print("Name is",r.name)
print("Marks are",r._student__marks)