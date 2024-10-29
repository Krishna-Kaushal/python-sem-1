# a=[98,23,43,53,45]
# b=sum(a)    #sum is a built in function in python 
# print(b)


# #creating  a function of percent calculator
# def func(a):
#     return sum(a)/5
# l1=[98,23,43,53,45]
# b=func(l1)
# print(f"The percentage marks is {b}")


# #print(),len(),range() etc. are built in functions in python
# def func(name):
#     print("Greetings!",name)

# func("harry")

# #taking multiple inputs in a function
# def func(a,b):
#     return a+b
# print(func(34,33))


# #default parameter/default argument
# def fun(name="krishna"):
#     print("Greetings!",name)
# fun("harry")   #it will greet harry
# fun()      #it will not  throw an error as a default name krishna is already in function,default will be used if 
# #           no argument is passed


# #recursion
# def func(n):
#     if n==1:
#         return 1
#     else:
#         return n*func(n-1)
    
# print(func(6))
# #a terminating condition is very important in recursions



#striping a given string
a="       this is krishna kaushal        "
print(a)
print(a.strip())