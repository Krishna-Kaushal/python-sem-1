def func(a,b,c):
    b= a+a*b*c/36500
    return round(b,2)


#testcase inputs
time_indays=789
principal=10000.0
rate=1.3
print(func(principal,rate,time_indays))