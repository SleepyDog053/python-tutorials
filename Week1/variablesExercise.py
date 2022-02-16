# Set myString to "hello", set myFloat to a float of 10.0 and set myInt to 20

myString = None
myFloat = None
myInt = None

# Testing code (do not delete or remove)
if myString == "hello":
    print(f"String: {myString}")
    print("myString is correct")
else:
    print('myString is not correct, make sure it is set to "hello"')
if isinstance(myFloat, float) and myFloat == 10.0:
    print(f"Float: {myFloat}")
    print("myFloat is correct")
else:
    print("myFloat is not correct, make sure it is set to 10.0")
if isinstance(myInt, int) and myInt == 20:
    print(f"Integer: {myInt}")
    print("myInt is correct")
else:
    print("myInt is not correct, make sure it is set to 20")
