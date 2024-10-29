#there are only two type of loops ->>  while and for

# i=0
# while i<10:
#     print("yes",i)
#     i+=1

# print("Done")

# #quick quiz   printing 1 to 50 using while
# i=1
# while i<=50:
#     print(i)
#     i+=1


# #printing content of  a list using while loop
# list=["banana","watermelon","mango","guava","grapes"]
# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1


# #use of "item" keyword in for loop
# l1=[1,7,8]
# for item in l1:        #item is predefined in list
#     print(item) 

# #use of "range" keyword in for loop
# for i in range(8):     #yah 0 se 7(n-1) tak hi jata hai
#     print(i)

# for i in range(1,8):   #left one inclusive ,right one exclusive i.e. 1 to 7(leap is 1)
#     print(i)

# for i in range(1,8,2):   #now it will also start taking leap of 2 after a print
#     print(i)
# #normally step size is rarely used in range keyword


# #for loop with else
# for i in range(10):
#     print(i)
# else:
#     print("this for loop syntax is rarely used.")
# #as soon as condition bexomes false ,else is executed


# #break statement ->>  as soon as  the program encounters break , it comes out of loop immediately
# for i in range(10):
#     print(i)
#     if i==5:
#         break
# else:
#     print("done")    #else part will not be printed as loop is not successfully executed


# #continue statement ->>  as soon as continue is encountered it will bypass the below part of the loop and start for
# #                        subsequent i+1
# for i in range(10):
#     if(i==5):
#         continue
#     print(i)
# #here 5 is not printed in output as after hitting continue,loop will restart for i+1


#declaring a null if statement in python(use of pass statement)
i=5
if(i==5):
    pass