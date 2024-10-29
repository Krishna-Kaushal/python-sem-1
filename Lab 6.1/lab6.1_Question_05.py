def func(a,b):
    for i in range(len(a)):
        if a[i]<0:
            a[i]=-a[i]
            b=b+1
    
    print(a)
    print(b)



#Driver inputs
l1=[1,2,-3,8,5,6,0,9]
print(l1)
func(l1,0)