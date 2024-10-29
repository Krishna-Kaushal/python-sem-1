a=int(input("Enter the retirement amount: "))
b=int(input("Enter the years of service: "))
if(b<5):
    a=a+0
elif(b<10 and b>=5):
    a*= 1.05
elif(b<20 and b>=10):
    a*= 1.1
else:
    a*= 1.2
print("Total retirement bonus: ",a)