a="Hello world"
b=a.strip()
print(b)
c=a.lstrip()
print(c)
d=a.rstrip()
print(d)
index=a.index("e")
print(index)
index=a.rindex("e")
print(index)

repl=a.replace("w","r")
print(repl)

split=a.split()
print(split)

join="-".join(a)
print(join)

center=a.center(20,"*")
print(center)

 
zfill=a.zfill(29)
print(zfill)

print("45".zfill(4))
# op-0045

ljust=a.ljust(20,"-")
print(ljust)

rjust=a.rjust(20,".")
print(rjust)

start=a.startswith("He")
print(start)

end=a.endswith("ld")
print(end)


