while True:
    print("MENU")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter you choice: "))
    if choice==5:
        break

    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    if choice==1:
        print(f"{a}+{b}={a+b}")
    elif choice==2:
        print(f"{a}-{b}={a-b}")
    elif choice==3:
        print(f"{a}*{b}={a*b}")
    elif choice==4:
        print(f"{a}/{b}={a/b}")
    else:
        print("Invalid input.")