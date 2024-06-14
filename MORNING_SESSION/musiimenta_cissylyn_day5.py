# Defining functions
#function syntax and parameters
#return values
#lambda functions

#example 1
#functions in python are defined using the def keyword
#followed by the function name and then the paratheses,insise the parathesis,you put a parameter
#and a colon.
# example  1
def multiply(x,y):
    return x*y
#calling the function
result =multiply(4,5)
print(result)

#example 2 multiple return values
def get_coordinates():
    return 10,20
x,y = get_coordinates()
print(x,y)
# exercise 1:define a function greet with a parameter name,set to guest,and print amessage
#i am a software engineer
def greet(name="guest"):
    print(f"iam a software enginner,{name}")

print(greet())
#exercise return with multiple values
def get_sentence():
    return "i am a software engineer","my name is musiimenta"
sentence_1,sentence_2 = get_sentence()
print(sentence_1,sentence_2)

#exercise 4:return your name and age as multiple values
def get_name_age():
    return "cissylyn",20
name,age = get_name_age()
print(name,age)

#notes
'''
def:keyword used to define a function
function_name:name of the function
parameter:optional,arguments passed to the function
docstrings:optional,describes the function purpose
return:optional,returns a value from the function
'''
#def function_name(parameter):
   # '''docstrings'''
    #function body
    #return value
    
    #lambda functions
    #lambda functions are small anonymous functions
    #can take any number of arguments but can only have one expression
    #syntax:lambda parameter:expression
    # example 5 create a lambda function that adds two numbers
def add(x,y):return x+y
print(add(4,5))

#example 6:use  cases of lambda fuction for sorting
coordinates =[(1,2),(2,3),(3,1),(5,0)]
coordinates.sort(key=lambda coordinate:coordinate[1])
print(coordinates)
#map,filter and reduce
#example 7:get the squares of 1 to 5 using map,filter and reduce
number_squares =[1,2,3,4,5]
square = list(map(lambda x:x**2,number_squares))
print(square)
       
    
    # exersice 5:define a function to get user info that accepts arbitary keyword argument and print 
    #each key value pair
def get_user_info(**kwargs):
    for key,value, in kwargs.items():
        print(f"{key}:{value}")
        get_user_info(name="cissylyn",age=20,year="year3")
    
    #exercise 6 use map to get the squares of 1 to 5
    def get_squares(numbers):
        return numbers**2