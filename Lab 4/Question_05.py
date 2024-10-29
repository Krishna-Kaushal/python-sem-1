a=int(input("Enter the intial capital: "))
b=int(input("Enter the rate: "))
c=int(input("Enter the time in years: "))
print("Enter the type of interest")
d=input("simple or compound: ")
if(d=="simple"):
    e=a+a*b*c/100
    print("%.2f"%(e))
elif(d=="compound"):
    e=a*pow((1+b/200),2*c)
    print("%.2f"%(e))
else:
    print("Invalid choice")