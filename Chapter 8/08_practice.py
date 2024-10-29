# #Question calculating greatest of three numbers by declaring func  without using max 
# def func(a,b,c):
#     if(a>b):
#         w1=a
#     else:
#         w1=b
    
#     if(w1>c):
#         print(f"{w1} is greatest.")
#     else:
#         print(f"{c} is greatest.")

# func(12,43,54)


# #Question  Celcius to farhenite by function
# def func(a):
#     return 1.8*a+32
# result=func(37)
# print("%.2f"%(result))


# #Question   prevent the print func to creating a new line in end (use of syntax: )   ,end=" "
# print("hello",end=" ")
# print("how",end=" ")
# print("are",end=" ")
# print("you",end=" ")

# def func(a):
#     if a==0:
#         return 0
#     else:
#         return a+func(a-1)
    
# print(func(100))


# #Question   printing a decreasing star pattern using recursion and without recursion
# def func(n):
#     if n==0:
#         None
#     else:
#         print("*"*n)
#         func(n-1)
# func(5)    

# n=5
# for i in range(n):
#     print("*"*(n-i))


# #Question  inches to centimeter conversion
# def func(a):
#     return 2.54*a
# n=10
# result= func(n)
# print(f"The {n} inches is {result} centimeter ")



# #Question    removing a specific word from a string and stripping it(not completed😅) 
# def func(a):
#     m1=a.replace("not"," ")
#     m2=a.strip()
#     print(m2)

# a="       Harry is not a good coder.He does not teach very well.         "
# func(a)


    


