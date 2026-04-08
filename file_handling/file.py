# file=open("manav.txt","w")
# file.write("hellO world")
# print(file)
# file.close()

#appand

# file=open("manav.txt","a")
# file.write("\nwelcome")
# print(file)
# file.close()

# #read
# file=open("manav.txt","r")
# z=file.read()
# print(z)
# file.close()

file=open("Mahabharat Wallpaper.jpg","rb")
con=file.read()
print(con)
file.close()

file_1=open("Mahabharat Wallpaper_copy.jpg","wb")
file_1.write(con)
print(file_1)
file_1.close()