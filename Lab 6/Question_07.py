def func(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum= sum+i
    return sum

n=int(input("Enter the number: "))
if(n==func(n)):
    print("1")
else:
    print("0")