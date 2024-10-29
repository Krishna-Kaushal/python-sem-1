#Creating a list using square brackets []
a= [1, 4, 7, 56, 33]
print(a[3])
#Modifying the list
a[3]=98
print(a)
#We can create a list with item of different type
b=[45, "Harry", False, 6.9]
#List Slicing
print(b[0:2])


#List Methods
list=[1, 8, 7, 2, 21, 15]
list.sort()      # It puts all elements in ascending order
list.reverse()   # It puts all elements in reverse order
list.append(45)  # adds something to the end of list
list.insert(1,544) #first one->>index and second one is new element to put in(Doesn't remover anything)
list.pop(3)      #deletes the 3rd index element
list.remove(15)  #deletes the element "15"
print(list)


#Tuples 
t=(1,2,4,5)
print(t[0])
#The key difference between tupple and list is that tuple can't be modified
# t[0]=9    #It will throw an error as tupple is immutable data type in python
a=()      #It will create an empty tuple ,printing empty tuple prints ()
a=(1,)    #Tuple with only one element needs a comma
print(a)


#Tuple methods in python
t=(1,2,1,4,5)
print(t.count(1))   #Kitni baar one aa rha hai
print(t.index(1))   #1(pahla wala) kis index par hai