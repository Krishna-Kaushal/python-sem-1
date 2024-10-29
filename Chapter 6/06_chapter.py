#If-else ladder collapse as soon as first if/elif satisfies
a=45
if(a>3):
    print("a is greater than 3.")
elif(a>7):
    print("a is greater than 7.")
elif(a>20):
    print("a is greater than 20.")
else:
    print("The a is neither greater than 3,7 nor 20")


# #Quick Quiz
# a=int(input("Enter the age: "))
# if(a>=18):
#     print("Yes")

age=45
if(age>34 and age<56):
    print("You can work with us.")
else:
    print("You can't work with us.")

#&& is given by "and" keyword
#|| is given by "or" keyword


#"is" and "in" keyword in python
a=None
if(a is None):
    print("True")
else:
    print("False")

a=[45, 56, 6]
print(45 in a)   #agar 45 'a' ke andar hai,toh yah true return karega
