num=13
print(id(num))
num=num+3
print(id(num))
num=num-3
print(id(num))
num="Hello"
print(id(num))

#The id function will not return the same value as of print function because it prints the address of variable in memory.