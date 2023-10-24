# lesson 12
# example 1
x = "hello"
y = "world"
z = x+y
print(z)

# example 2
x = "hello"
y = "2"
z = x+y
print(z) # or you can do
x = "hello"
y = 2
z = (x,y) #concat or concatonate
print(z)

# example 3
name = input("what is your name")
print("hello",name)
# if you want first litter capital
name = input("what is your name")
print("hello",name.capitalize()) # changes bob to Bob
print("hello",name.title()) # changes bob smith to Bob Smith
print(name.count("e")) # only count small e in my name
print(name.find("e")) # finds where the first e is, -1 if not found
print(name.isdigit()) # checks if te name string is only number
print(name.isalpha()) # checks if the name string is only a to z
print(name.islower()) # checks is it only small letters
print(name.isupper()) # checks if capitals
print(name.isalnum()) # checks only a-z and 0-9
print(name.lower()) # changes to all small
print(name.upper()) # changes to all capital
print(name.replace("e","x"))
print(name.replace("e","x").replace("l","1"))
quit()


