# #Question  creating a dictionary with hindi words translated for foolish english speakers
# mydic={
#     "Pankha":"Fan",
#     "Dabba":"Box",
#     "Vastu":"Item"
# }
# print("Options are",mydic.keys())
# a=input("Enter the hindi word: ")
# # print("The meaning of your word is:",mydic[a])   #will throw an error if it is unfound
# print("The meaning of your word is:",mydic.get(a)) #will return none if not found


# #Question  Taking 8 numbers as input an printing unique ones
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=int(input("Enter a number:"))
# d=int(input("Enter a number:"))
# e=int(input("Enter a number:"))
# f=int(input("Enter a number:"))
# g=int(input("Enter a number:"))
# h=int(input("Enter a number:"))
# s1={a,b,c,d,e,f,g,h}  
# print(s1)
# #jab bhi unique ones ki baat ho go for set


# #Question  Can a set have 18(int) and "18"(string) as values
# s={18,"18"} 
# print(s)  
# #so yes,for python 18(int) and 18(str) is different items


# #Question   Detecting length of following set
# s1=set()
# s1.add(20)
# s1.add(20.0)
# s1.add("20")
# print(len(s1))
# #20 and 20.0 is taken as same to set due to their numeric equality

# #Question   Create an empty dictionary.Allow four friends to enter their
# #           favourite languages as values and use their names as keys.
# dic={}
# a=input("Enter your favourite language Shubham \n")
# b=input("Enter your favourite language Ankit \n")
# c=input("Enter your favourite language Sonali \n")
# d=input("Enter your favourite language Harshita \n")
# dic["Shubham"] =a
# dic["Ankit"] =b
# dic["Sonali"] =c
# dic["Harshita"] =d
# print(dic)

# #if two names are same in above then recent one will be finalised
# #if languages are same nothing happens 
# #this proves that values may be same, but keys must be unique


#Question   tupples can't be modified within the set

