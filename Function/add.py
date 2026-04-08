# def add(a,b):
#     return a+b
# res=add(2,3,4)
# print(res)
# def add(*a):
#     return sum(a)
# res=add(2,3,4,5)
# print(res)

def add(x,/):
    return sum(x)
res=add((7,13,1))
print(res)