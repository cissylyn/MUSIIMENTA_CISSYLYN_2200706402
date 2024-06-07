''' 
control structures
conditional statements
loops(for,while
compresions(lists,dictionary,compressions))
'''
# Example 1
print("........example 1..........")
age = 23
if age > 65:
    print("you are a senior citizen")
elif age > 18:
    print("you are an adult")
else:
    print("you are a youth")

# Example 2
print("........example 2..........")
grade = 88
if grade >= 90:
    print("excellent")
elif grade >= 80:
    print("very good")
elif grade >= 70:
    print("good")
else:
    print("not good")

# Exercise
 # price of movie based on age 
 # under 13,price shs1000, between 13 and 18 price shs 500, 18 and above pay full price shs 2000,
#senior citizens shs 5000
print("........exercise..........")
ages = 13
if ages > 65:
    print("pay 5000 shs")
elif ages >= 18:
    print("pay 2000 shs")
elif 13 <= ages < 18:
    print("your discount is 500 shillings")
else:
    print("your discount is 1000 shillings")
#loops
# loops iterates over  a sequence (list,tuple,dictionary etc)
# while loop ..repeats as long as the condition is true
#example 3

print("............example 3...............")
cars =['tesla','Audi','BMW','jeep','RangeRover']
for car in cars:
    print(car)
print('............exercise 2...........')

#  ,create the reverse of the input 12345 using while loop
# create your own list of your favcolors using a for loop
favourite_Colors = []
print('............................favourite colours...............................................')

for color in ["blue", "green", "purple", "orange", "yellow"]:
    favourite_Colors.append(color)

print(favourite_Colors)

print(".............................rerve...............................")
input_number = "12345"


reversed_number = ""


index = len(input_number) - 1


while index >= 0:
    reversed_number += input_number[index]
    index -= 1

print("Reversed number is:", reversed_number)
