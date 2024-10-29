n = int(input("Enter the number of rows: "))
k = 1
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + k), end=" ")
        k += 1
    print()
