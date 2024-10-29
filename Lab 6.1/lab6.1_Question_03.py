import math

def func(n):
    count=0
    l1=[]
    for i in range(1,n+1):
        if int(math.sqrt(i))**2==i and int(round(math.pow(i,1/3),2))**3==i:
            l1.append(i)
            count+=1

    return count,l1

#Driver inputs
n=1000
a,b = func(n)
print(f"Desired numbers are {b} and total count is {a}")