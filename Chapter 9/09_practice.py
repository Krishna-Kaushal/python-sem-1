# #Question1: checking whether the file poem.txt contain word "twinkle" or not
# f=open("poem.txt","r")
# t=f.read()
# if "twinkle" in t:
#     print("Twinkle is there.")
# else:
#     print("Twinkle is not there.")
# f.close


# #Question2: Updating High score program
# def game():
#     return 464

# with open("HighScore.txt") as f:
#     HighScore=f.read()

# score =game()
# if HighScore=="":
#     with open("HighScore.txt","w") as f:
#         HighScore=f.write(str(score))
# elif int(HighScore)<score:
#     with open("HighScore.txt","w") as f:
#         HighScore=f.write(str(score))


#Question3: Program to generate multiplication table from 2 to 20 and write it in diff files and place in a folder
for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}.txt","w") as f:
        for j in range(1,11):    
            f.write(f"{i}*{j}={i*j}")
            if j!=10:
                f.write("\n")                        #this will kill the 11th blank line that will be created
    

# #Question4: Replacing word "Donkey" in a file with "######"
# with open("donkey.txt") as f:
#     content=f.read()
# content=content.replace("Donkey","######")
# with open("donkey.txt","w") as f:
#     content=f.write(content)

# #Question5: You are given a list of abusive words like donkey
# word=["donkey","kaddu","mote","bhosdiwale"]
# with open("donkey.txt") as f:
#     content=f.read()
# for item in word:
#     content=content.replace(item,"######")
# with open("donkey.txt","w") as f:
#     content=f.write(content)


# #Question6: Mine a log file and check whether it contains "python" or not
# with open("log.txt") as f:
#     content=f.read()
# if "python" in content.lower():
#     print("Yes, python is there.")
# else:
#     print("python is not there.")

#Question7: find the line that has that python word

# #Question8: Making a copy of a existed file
# with open("poem.txt") as f:
#     content=f.read()

# with open("copy_of_poem.txt","w") as f:
#     f.write(content)

# #Question9: Checking whether 2 files are identical or not
# with open("donkey.txt") as f:
#     f1=f.read()
# with open("poem.txt") as f:
#     f2=f.read()
# if f1==f2:
#     print("Files are identical.")
# else:
#     print("files are different.")

# #Question10: Wiping out all content of a file
# with open("sample.txt","w") as f:
#     f.write("")


#Question11: Renaming a file name (basically u make a copy and delete the original one)
import os
with open("sample.txt") as f:
    content=f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(content)
os.remove("sample.txt")