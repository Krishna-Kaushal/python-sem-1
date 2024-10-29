n=int(input("Enter the number: "))

if n<98:
    for i in range(n+1):
        if i%5!=0:
            print(i)

else:
    print("Invalid input")