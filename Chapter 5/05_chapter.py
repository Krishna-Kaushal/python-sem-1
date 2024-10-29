#Introduction to dictionaries:
myDic={
    "Fast": "In a quick manner",
    "Harry":"A coder",
    "Marks":[1,2,4]
}
print(myDic["Fast"])
print(myDic["Marks"])
#Dictionaries are unordered


#Nested Dictionaries
dic={
    "anotherdic":{"harry":"coder"}
}
print(dic["anotherdic"]["harry"])


#Keys within a dictionary can be modified 
myDic["Marks"]=[45,78]
print(myDic)

#Dictionary methods
print(myDic.keys())    #display all the keys defined within the dictionary
print(myDic.values())  #display all the values paired to corrosponding keys
print(myDic.items())   #print the (key,value) pairs for all the contents of dictionary

dict2={
    "Lovish":"Friend"
}
myDic.update(dict2)   #adds new pairs of dict2 to the myDic dictionary and can update if prexists
print(myDic)

#Difference between .get and [] syntax in dictionary methods
# print(myDic["harry2"])       #Throws an error if key harry2 is not present
print(myDic.get("harry2"))   #Returns "none" as output if harry2 is not present




#Sets(a collection of non repetetive elements) in python
a={1,3,4,1,5}
print(a)   #Sets merges repetetive items into one item

a={}    #It will create an empty dictionary not an empty set
print(type(a))
#An empty set can be created by using below syntax
b=set()
print(type(b))


b.add(4)         #add items to a set
b.add(4)         #adding a value repetetively will not add it more times
# b.add([5,6,7])   #lists can't be added to set, will throw an error, dictionaries also can't
b.add((5,6,7))   #Tuples can be added to set
#Unhasable means non permanant


print(len(b))  #prints the length of the set
b.remove(4)    #Removes a specific element from the set
# b.remove(15)   #Throws an error as 15 is not even in set
b.pop()        #Removes an arbritray element from set
b.clear()      #Delete all elements within set





