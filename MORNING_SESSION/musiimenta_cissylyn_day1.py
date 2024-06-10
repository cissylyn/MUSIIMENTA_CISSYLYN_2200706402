


# this is a comment 


x = 5  
y = "Hello, World!"
print(y,x) # we concatenate a string and number using a comma


print("hello world") # this is how we print in python

"""
This is amulti-line comment
"""

'''
this is also a multi -line 

'''
if 10 > 1:
  print("ten  is greater than one!")# in python identation is used to indicate a block of code
  x = 5  
print(type(x)) # this prints the datatype of any object

      
y = "cissy" # x is now of type str
print(type(y))

x, y, z = "car", "benz", "subaru"
print(x)# print car
print(y)#print benz
print(z)#print subaru

x = "awesome"   # this a global variable

def myfunc():
  print("Home is" + x)

myfunc() #calling of the function


def myprac():
  global x  # this is also a global variable beacause it is declared with a global keyword
  x = "fun"

myprac()

print("your are" + x)


x = int(1)   # x will  be casted to be 1
y = int(2.8) # y will be casted to be 2
z = int("3") # z will be casted be 3


print("It's alright") #use of double quotes to print a string
print('He is called Johnny')#use of single quotes

names = ["cissy", "lyn", "ciara"]
x = names[0]#returns cissy
y = len(names)#returns the length of the array

for x in names:
  print(x) # loops through an array
  
 
 








