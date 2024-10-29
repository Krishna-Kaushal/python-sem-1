def func(a):
    words=a.split()
    even_words=[]
    for word in words:
        if(len(word)%2==0):
            even_words.append(word)

    return even_words

a=input("Enter sentences: ")
print("Extracted even length words are: ",func(a))