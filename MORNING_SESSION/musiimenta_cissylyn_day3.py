
# python operators
''' 
name of the operator     symbol with example
addition                     x + y
subtraction                  x - y
multiplication               X *  y
division                     X /Y
modulus                      X % Y
exponentiation              X ** Y
floor division              X//Y

COMPARISON OPERATORS
name of the operator           symbol with example
Equal                           ==
Not equal                       X != Y
Less than                       X <Y
greaterthan                     x > Y
Less than or equal to           x <= y
greater than or equal to        x >= y
LOGICAL OPERATORS
name of the operator            symbol
and                              and   
or                               or       
not                               not 

MEMBERSHIP OPERATORS
in                    x in y
not in                 x not in y   
BITWISE OPERATORS
name                         symbol
AND                            &
OR                             |
XOR                             ^
NOT                             ~

#python cases
1.snake_case
2. camelCase
3.UpperCase  
4.kebeb-case  
'''
# compresions(list,dictionary,compresion)
"""compresion provide a concise way to create lists and dictionaries
what is the symbol
lists           [] square brackets  used to store multiple items in a single variable
dictionaries    {} curly brackets used to store data values in key:value pairs

"""
#example one basic list comprehensions
# create a list of squares in range of 10

list_of_squares =[x**2 for x in range(10)]
print(list_of_squares)

# exercise 1 
# create a list of evensquares in the rage of 20
list_of_even_squares =[x**2 for x in range(20) if x%2 ==0]
print(list_of_even_squares)

# example 2 : dictionary comprehension
# create a dictionary compresion for favourite cars ,count the length of the charaters
favourite_cars =['BMW','jeep','mercedes','fordraptor']
car_lengths ={car:len(car) for car in favourite_cars}
print(car_lengths)

# exercise 2: create a list of tuple where each tuple contains a number and its cube for numbers
#between 1 and 10  using a dictionary comprehension
number_cubes = [(x, x**3) for x in range(1, 11)]
print(number_cubes)
