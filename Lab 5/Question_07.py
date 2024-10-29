sum=0
n=int(input("Enter how many students? "))
print("Enter age: ")
for i in range(n):
    a=int(input())
    sum+=a
print("The average age is: ",sum/n)   