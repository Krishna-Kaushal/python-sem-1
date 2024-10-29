def func(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i

    if sum==a:
        return True
    else:
        return False

n=int(input("Enter a positive integer: "))
l1=[]
for j in range(1,n+1):
    if func(j):
        l1.append(j)

print("Perfect numbers are: ",l1)