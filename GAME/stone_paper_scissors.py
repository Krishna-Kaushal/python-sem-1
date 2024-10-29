import random
a=random.randint(1,3)    # choose anything between 1 to 3 both inclusive

if a==1:
    comp="st"
elif a==2:
    comp="p"
elif a==3:
    comp="sc"

b=input("Your choice: stone(st),paper(p),scissors(sc) ?")

def func(comp,you):
    if(comp=="st" and you=="p"):
        print("computer chose stone , you won!😎")

    elif(comp=="st" and you=="sc"):
        print("computer chose stone , you lost!😂")

    elif(comp=="p" and you=="st"):
        print("computer chose paper , you lost!😂")

    elif(comp=="p" and you=="sc"):
        print("computer chose paper , you won!😎")
        
    elif(comp=="sc" and you=="st"):
        print("computer chose scissors, you won!😎")

    elif(comp=="sc" and you=="p"):
        print("computer chose scissors, you lost!😂")

    else:
        print("It's a draw!🧐")


func(comp,b)
    