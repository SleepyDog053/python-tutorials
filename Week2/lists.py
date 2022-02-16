# lists contain any type of variable and can be full of variables

myList  = []

# Add to the list with append
myList.append(1)
myList.append(2)
myList.append(3)

# View the list with the below, remember lists start at 0 not 1
print(myList[0]) # Will print 1
print(myList[1]) # Will print 2

for x in myList:
    print(x)

# Make a list of fruits, and add "banana", "orange" and "apples"
# Then print only orange