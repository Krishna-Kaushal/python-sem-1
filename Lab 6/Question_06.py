def func(x,y):
    z=y/100
    return x/(z*z)
a=int(input("Enter the height in centimeters: "))
b=int(input("Enter the weight in kilograms: "))
c=func(b,a)
if c<18.5:
    print("Underweight")
elif c>=18.5 and c<=24.9:
    print("Normal")
elif c>24.9 and c<=29.9:
    print("Overweight")
else:
    print("Obese")

print(round(c,1))