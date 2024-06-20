#example 1: create aclass where a dog inherits from animal and overrides with a speak method
class Animal:
    def speak(self):
        return "meow"
    
class Dog(Animal):
    def speak(self):
        return "bark"
#implementation of inheristance
Animal = Animal()
dog = Dog()

print(Animal.speak())
print(dog.speak())
# polymorphism allowing a method to do different things based on the object that it is acting upon
#polymorphism allows objects of different classes to be treated as objects of the a common super class
#method resolution order(MRO) is the order in which classes are searched in method resolution
#example 2:how polymorphism works in python
class Animal:
    def speak(self):
        return "talk"
    
class Dog(Animal):
    def speak(self):
        return "barking"
    
class cat(Animal):
    def speak(self):
        return "meow"
def make_animal_speak(animal):
    return animal.speak()
make_animal_speak(Dog())



#create a simple application to manage different types of vechicles
# derive a class to demonstrate inheristance and polymorphism
#requirements base class vechicle ,attributes make,model.method display information
# the derived class can be car inheristances from vechicle and attributes are no of doors
#the overrides the display information method to include the number of doors
#other derived class motorcycle ,attributes are type of bike(cruiser,sport,touring) and  overrides the display information method

# create a function that takes a list of vechicles and displays information about each vechicle to print details about each vechicle
class Vechicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def display_info(self):
        return f"make:{self.make},model:{self.model}"
    
class Car(Vechicle):
    def __init__(self,make,model,doors):
        super().__init__(make,model)
        self.doors = doors
    def display_info(self):
        return f"make:{self.make},model:{self.model},doors:{self.doors}"
    
class Motorcycle(Vechicle):
    def __init__(self,make,model,bike_type):
        super().__init__(make,model)
        self.bike_type = bike_type
        
    def display_info(self):
        return f"make:{self.make},model:{self.model},bike type:{self.bike_type}"
    
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())
        
Vechicle =[Car("Toyota","corolla",4),Motorcycle("pikipiki","model 1","sport")]
display_vehicle_info(Vechicle)
    

"""
working with textfiles
handling a csv file
json and xml file processing
"""
#working with text files,open,read,write and close
'''
-- description
 opening File:use an open function open()(r-read,w-write,a-append,r+read and write)
    reading file:use the read method read()
    writing to a file:use the write method write()
    closing a file:use the close method close()
'''
#example 3:write afile and read a file
# wrinting to a text file
with open("cissy.txt","w") as file: 
    file.write("am cissylyn , i love python. \n")
    file.write("i am a software developer")

#reading from a text file
with open("cissy.txt","r") as file:
    content = file.read()
    print(content)
    
    
    # handling csv files
    '''
    csv( comma separated values) files are used to store tabular data in plain text
    it helps in protecting the intergrity of the data
    key concepts :
    reading csv files: using "csv.reader" to read csv files
    writing csv Files:using "csv.writer" to write csv files
    DictReader and DictWriter:used to read and write csv files as dictionaries
    
    '''
    # example 4: writing and reading csc files
    import csv 
    # writing to a csv file
    with open("cissy.csv","w",newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name","age","location"])
        writer.writerow(["cissy","23","kampala"])
        writer.writerow(["lyn","25","kampala"])
        
#reading from a csv file
with open("cissy.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        
#handling json files
'''
json  files are used to store data in a key value pair
json in full is javascript object notation
xml in full is extensible markup language
they are used for structuring data
key concepts:
loading JSON:using json.load() to reading json file
Dumping JSON:using json.dump() to write json file
parsing JSON:using json.loads()  for handling json strings

'''
# example 6 write and read json files
import json
#wrinting to json file
student_data = {
    "name":"cissy",
    "age":23,
    "location":"kampala",
    "year" :"2024"
}
#open the file
with open("cissy.json","w") as jsonfile:
    json.dump(student_data,jsonfile)
#reading from a json file
with open("cissy.json","r") as jsonfile:
    data = json.load(jsonfile)
    print(data)
    #exercise 2:write and read an xml file
    import xml.etree.ElementTree as ET
    #writing to an xml file
    root = ET.Element("student")
    name = ET.SubElement(root,"name")
    name.text = "cissy"
    age = ET.SubElement(root,"age")
    age.text = "23"
    location = ET.SubElement(root,"location")
    location.text = "kampala"
    year = ET.SubElement(root,"year")
    year.text = "2024"
    tree = ET.ElementTree(root)
    tree.write("cissy.xml")
    #reading from an xml file
    tree = ET.parse("cissy.xml")
    root = tree.getroot()
    for child in root:
        print(child.tag,child.text)
        
    
    
    # exercise 3 :using abstraction calculate the area and perimeter of a rectangle
        #abstract class
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
    def display(self):
        print("area:",self.area())
        print("perimeter:",self.perimeter())
def main():
    rectangle = Rectangle(10,20)
    rectangle.display()
    
    

