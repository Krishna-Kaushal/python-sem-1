a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
x=int(input("Enter the value of x: "))
k=int(input("Enter the value of k: "))
print("\n")
if(x>k):
    y=a*pow(x,2)-b*x+c
    print(y)
elif(x<k):
    y=a*pow(x,2)+b*x+c
    print(y)
else:
    y=0
    print(y)