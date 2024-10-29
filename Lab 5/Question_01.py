n=int(input("Enter the number: "))

product=1
while n!=0:
    product= product *(n%10)
    n=n//10
   
print(product)  