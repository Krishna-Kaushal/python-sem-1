def func(a):
    flag=1
    for j in range(len(a)):
        for i in range(len(a)):
            if a[j]==a[i] and i!=j:
                flag=0
                break
    if flag==1:
        return True
    else:
        return False
    
            
            
n=int(input("Enter the length of list: "))
l1=[]
for i in range(n):
    ele=int(input())
    l1.append(ele)
print(l1)
print(func(l1))

