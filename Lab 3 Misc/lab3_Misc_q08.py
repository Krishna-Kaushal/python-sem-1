n=int(input("Enter your rating on the platform: "))

if n>2100:
    print("Grandmaster")
elif n>1900:
    print("Candidate master")
elif n>1600:
    print("Expert")
elif n>1400:
    print("pupil")
else:
    print("newbie")