def func(a):
    if a<=100 and a>=1:
        return a*(a+1)*(2*a+1)/6
    else:
        print("Invalid input.")

#testcase inputs
n=6
print(func(n))