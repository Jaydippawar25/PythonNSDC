select=input("Enter the opertaor(+,-,*,/,//,%,**): ") 
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))

def cal(a,b,select):
 
    if select=="+":
        return a+b
    elif select=="-":
        return a-b
    elif select=="*":
        return a*b
    elif select=="/":
        return a/b
    else:
        print("Invalid opr") 
res=cal(a,b,select)
print(res)

