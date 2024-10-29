a=float(input("Enter the principal amount:"))
b=float(input("Enter the rate :"))
c=float(input("Enter the time in consideration :"))
d=a*pow((1+b/100),c)-a
print("\n")
print("The compound interest (excluding intial capital) is %.2f "%(d))
