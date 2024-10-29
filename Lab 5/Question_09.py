a=int(input("Enter the starting number: "))
r=int(input("Enter the common ratio: "))
n=int(input("Enter the number of terms: "))
for i in range(n):
    print(a*pow(r,i),end=" ")