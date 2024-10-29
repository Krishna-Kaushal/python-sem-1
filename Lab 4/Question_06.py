ch=input("Enter the character: ")
a=ord(ch)
if(a<=57 and a>=48):
    print("Digit")
elif(a<=90 and a>=65):
    print("Uppercase")
elif(a<=122 and a>=97):
    print("Lowercase")
else:
    print("Special Chracter")