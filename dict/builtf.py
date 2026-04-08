student={
        "Name":"ram",
        "age":23,
        "Contact":3445677
    }
print(student)

#add
print(student["Name"])
student["Adhar"]="1234 5678 9012"
student["email"]="ram21@gmail.com"

#update
print(student)
student["age"]=18
print(student)

#get
print(student.get("Name"))

#items()
print(student.items())

#keys()
print(student.keys())

#pop
student.pop("Adhar")
print(student)

#del
del student["email"]
print(student)