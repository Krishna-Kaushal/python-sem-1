a="harry"
b=16
c=36.68
d=False
e=None
#keywords are predefined words in python.

#Printing the variables
print(a)
print(b)
print(c)
print(d)

#Printing the variable type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#Variable name can't be started with digit

#Operators in python
a=3
print("The value of 3+4 is ",3+4)
print("The value of 3-4 is ",3-4)
print("The value of 3*4 is ",3*4)
print("The value of 3/4 is ",3/4)
a+=7
print("The value of updated a is ",a)

#Comparison Operators
b=(14>7)
print(b)

#Logical Operators
bool1=True
bool2=False
print("The value of bool1 and bool2 is",bool1 and bool2)
print("The value of bool1 or bool2 is ",bool1 or bool2)
print("The value of not on bool1 is ",not bool1)

#Typecasting
a="3535" #(String)
a=int(a) #(Typecasting)
print(type(a))
print(a+5)
b=str(32)
print(type(b))

#Taking input from the user
a=int(input("Enter your name \n"))
a=int(a)  #typecast string into integer
print(a)
print(type(a))

#Pretypecasting
a=int(input("Enter your age:"))