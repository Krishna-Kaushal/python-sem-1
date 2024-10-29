C=int(input("Enter the cost price: "))
S=int(input("Enter the selling price: "))

if C<S:
    print("1")
    print(S-C)
else:
    print("0")
    print(C-S)
