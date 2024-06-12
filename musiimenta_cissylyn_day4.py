# dictionaries
#creating and using dictionaries
# dictionary methods and operations
'''
Dictionaries in python are collections of keys and values
unordered
mutable and indexed by keys

'''
# example 1:create a dictionary
#create a dictionary for a student persuing software engineering
#the key must be your name,age,technology interest,course and year of study
# you own details

student_dict ={
    'name':'cissylyn',
    'age':'20',
    'technology':'AI and ML',
 
    'course':'BSE',
    'year':'year3'
    
}
# access values
print(student_dict['name'])
print('..........................exercise 1.....................')
# exercise 1
# modify age and technology
student_dict['age'] = 50
print(student_dict)

#adding keys and values
student_dict['email'] ='musiimentacissylyn7@gmail.com'
print(student_dict)
print('...........................exercise 2...................')
# exercise 2
#  remove a key and value from the student dict

# Remove the 'technology' key and its value
del student_dict['technology']

# Print the modified dictionary
print(student_dict)

#common dictionary methods
'''
get()    returns the value for the specified key if the key is in the dictionary.if not
it returns the dafault value
update()    updates the dictionary with elements from another dictionary
pop()       removes the specified key and return the corresponding value

'''
print('..........................example 3.............................')
# example 3:Use the get method to get a value
print(student_dict.get('technology'))


print('............................exercise 3............................................')
#update any valuein ageusing the update method
student_dict.update({'age': '21'})  

print(student_dict)

print(".........................exercise 4...................................")
#use if to check if the key is present in the dictionary

if "age" in student_dict:
   print('age is present')
else:
    print('age not found')


#keys ,values()and items() method
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

'''
keys()returns a return a view of objects that displays a list of all keys
values()returns a view of objects that displays a list of all values
items()returns a view of objects that displays a list  of dictionary keys and
values tuple pairs
'''
# use the update method to change the course and a new key whatsapp number
print("..........................exercise 5.....................")
student_dict.update({'course': 'Computer Science', 'whatsapp_number': '1234567890'})
print(student_dict)



