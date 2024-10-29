a=int(input("Enter the length of first side: "))
b=int(input("Enter the length of second side: "))
c=int(input("Enter the length of third side: "))
if(a+b>c and b+c>a and c+a>b):
    print("This is a triangle")
    if(a==b or b==c or a==c):
        print("And it's isosceles")
    else:
        print("Not isosceles")
else:
    print("Not a triangle")