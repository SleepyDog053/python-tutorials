# Programming is built on making decisions
# For this we use operators and set conditions which are then compared with "if" and "else"

if (1==1):
    print("1 is equal to 1")

# elif exists if you want to make sure the above is not true, try this

a = 33
b = 33

if (b > a): 
    print("b is greater than a")
elif (b == a):
    print("b is equal to a")

# Use else if none of them are met

if (b > a):
    print("b is greater than a")
elif (b == a):
    print("b is equal to a")
else:
    print("b is less than a")

# We can also combine conditions with "and" and "or"

a = 11
b = 22
c = 33

if (a > b) and (a > c):
    print("a is the biggest")
elif (a < b) and (a < c):
    print("a is the smallest")
else:
    print("a is the middle number")

# Try using or and predictinng the output