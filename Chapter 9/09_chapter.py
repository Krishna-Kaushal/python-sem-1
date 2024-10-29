# #using open function to read content of a file
# f=open("sample.txt","r")   # classical method 
# f=open("sample.txt")       # if no mode is mentioned , by default it is r
# data=f.read()   # if nothing mentioned inside braces, it will read all chracters.
# data=f.read(2)  # only reads first 2 characters
# print(data)
# f.close()

# #Other methods to read the files(use of readline func)
# f=open("sample.txt")
# data=f.readline()  # reads first line
# print(data)
# data=f.readline()  # reads 2nd line now
# print(data)
# f.close

# #Other mode w(for writing), a(for appending), +(for both reading and writing)
# f=open("sample.txt","w")
# f.write("It will clear everything written before and this will be updated text within")

# f=open("sample.txt","a")
# f.write("I am appending.")  #appending means file ke last mein kuchh likhna

# f.close()

#use of with(no  f.close  required here)
with open("sample.txt","r") as f:
    a=f.read()
with open("sample.txt","w") as f:
    a=f.write("Me")
print(a)
#best way to open and close a file automatically is with "with statement"
#Try to use with statement always