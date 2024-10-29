print("Enter the booking type")
a=input("online, advanced, spot/window: ")
print("Enter the car brand")
b=input("Toyota, Honda, Hyundai, Suzuki, Tata: ")
d=0
if(a=="online"):
    if(b=="Toyota"):
        d=25000*0.9
    elif(b=="Honda"):
        d=35000*0.9
    elif(b=="Hyundai"):
        d=45000*0.9
    elif(b=="Suzuki"):
        d=60000*0.9
    elif(b=="Tata"):
        d=80000*0.9
    else:
        print("No such Brand")
elif(a=="advanced"):
    if(b=="Toyota"):
        d=25000*0.92
    elif(b=="Honda"):
        d=35000*0.92
    elif(b=="Hyundai"):
        d=45000*0.92
    elif(b=="Suzuki"):
        d=60000*0.92
    elif(b=="Tata"):
        d=80000*0.92
    else:
        print("No such Brand")    
elif(a=="window" or a=="spot"):
    if(b=="Toyota"):
        d=25000
    elif(b=="Honda"):
        d=35000
    elif(b=="Hyundai"):
        d=45000
    elif(b=="Suzuki"):
        d=60000
    elif(b=="Tata"):
        d=80000
    else:
        print("No such Brand")
            
else:
    print("Invalid option") 
    
print("Bill amount is %.1f"%(d))