#Taking input as name and wishing them good Afternoon
a=input("Enter your name: ")
b="Good afternoon "
print(b+a) 
print("Good Afternoon",a)


#Question2 Completing the letter
letter='''Dear <|NAME|>,
You are selected 

Date: <|DATE|>'''
name=input("Enter your name: \n")
date=input("Enter the date: \n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)


#Question3 Detecting double spaces in a string
st="This is a string with  double spaces"
a=st.find("  ")
if(a!=-1):
    print("True")
else:
    print("False")


#Question4 Replacing the double space with single in previous question
st=st.replace("  "," ")
print(st)


#Question5 Formating a letter
letter= "Dear Harry, This Python course is nice! Thanks!"
formatted_letter="Dear Harry, \n\tThis python course is nice!\nThanks!"
print(formatted_letter)