#Concatenating two strings
greeting = "Good Morning"
name = " Krishna Kaushal"
c= greeting + name
print(c)


#String Slicing
name="harry"
print(name[1])
print(name[0:3])  #It will exclude 3, left inclusive , right exclusive
sl=name[0:3]
print(sl)
print(name[:4])   #It will start from first i.e. 0:3
print(name[0:])   #It will auto include upto last


#Negative indices are used when we don't know the length of the string
print(name[-1])   #It will print first element from the last


#Slicing with Skips
name="HarryisGood"
print(name[0::3])   #It is same as 1:10:3. It will simply print H leave 2(n-1) and then again print and so on


#StringStory
story="once upon a time there was a youtuber named Harry who uploaded python course with notes"
print(len(story))   #prints the length of the string i.e. counts all elements in string including the spaces
print(story.endswith("ote"))   #kya string ke last mei ote hai nahi, "otes" hai, so false is printed
print(story.count("se"))   #It counts how many times this particular thing occur in whole string
print(story.capitalize())  #It capitalise the first element of whole string
print(story.find("once"))  #If true tells the position of first occurance(can be 0 as first), if false it reports -1
print(story.replace("Harry","CodewithHarry"))


#EscapeSequences  ->>  \n ,\t etc are known as escape sequence characters
story="Harry is good.\nHe\t is very good"
print(story)