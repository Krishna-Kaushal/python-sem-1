#creating a 2D list, initializing all to zero 
columns=8
rows=5
matrix=[[0 for x in range(columns)] for y in range(rows)]
print(matrix)


#you can now add items to the list matrix[col][row]
matrix[0][0]=1
matrix[0][6]=2
print(matrix[0][0])
print(matrix)

# printing a diamond using star pattern
n = 9
for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()

for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
    for a2 in range(a1 - (n+1)//2):
        print(" ", end = "")
    for a3 in range((n+1 - a1)*2 - 1):
        print("*", end = "")
    print()