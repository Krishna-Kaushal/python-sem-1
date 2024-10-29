def func(a):
    flag=1
    for i in range(2,a):
        if a%i==0:
            flag=0
        
    if flag:
        print("Yes")
    else: 
        print("No")


n=int(input("Enter a number: "))
if n<=100:
    func(n)
else:
    print("Invalid input.")