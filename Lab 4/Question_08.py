a=int(input("Enter the distance in kilometers: "))
if(a<=50):
    b=a*7
elif(a>50 and a<=100):
    b=350+(a-50)*10
else:
    b=350+490+(a-100)*15
print("The total fare is: ",b)
