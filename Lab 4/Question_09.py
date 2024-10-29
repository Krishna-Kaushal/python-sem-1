print("Enter the type of flight")
a=input("international or domestic: ")
print("Enter the type of payment")
b=input("prepaid or at airport: ")
c=int(input("Enter the weight of baggage: "))

if(a=="domestic"):
    if(b=="prepaid"):
        if(c<=3):
            d=1350
        elif(c<=5 and c>3):
            d=2250
        elif(c<=10 and c>5):
            d=4500
        elif(c<=15 and c>10):
            d=6750
        elif(c<=20 and c>15):
            d=9000
        else:
            d=13500
    else:
        d=550*c

else:
    if(b=="prepaid"):
        if(c<=3):
            d=2750
        elif(c<=5 and c>3):
            d=5520
        elif(c<=10 and c>5):
            d=8280
        elif(c<=15 and c>10):
            d=11040
        elif(c<=20 and c>15):
            d=16560
        else:
            d=600
    else:
        d=600*c

print(d)


