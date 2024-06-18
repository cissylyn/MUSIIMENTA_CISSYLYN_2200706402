#error handling
# exception handling with try and except
#custom exception handling
'''
error handling in python helps you to handle errors that might occur in your code
!. try block:contains the code that might raise an exception
2. except block:contains the code that handles the exception
3. finally block:contains code that will always run regardless of the result,used for clean up code
Nb you can speciffy different handlers for different exceptions types
3. else block:contains code that will run if the try block does not raise an exception
if no exception raised in the try block,it runs the else block
'''
#example 1:handle exceptions with division by zero
try:
    number =  int(input("enter a number:"))
    result = 10/number
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(result)
finally:
    print("code executed successfully")
 # exercise 1: write a function that converts a string to an integerand handle both value error if the string cannont be converted into an interger
#and type error if the input is not a string
#use multiple except blocks to handle the different types of exceptions
#capture input from the user
    def convert_string_to_int(string):
      try:
        number = (input("enter a number:"))
        result = int(number)
        print(result)
      except ValueError:
        print("please enter a valid")
      except TypeError:
        print("please enter a string")
      else:
        print(result)
      finally:
        print("code executed successfully")
     
convert_string_to_int("string")
# custom exception handling
#example 2 :exception raised for error inthe input ,if funds are insufficient
class InsufficientFundsError(Exception):
    def __init__(self, balance,amount):
        self.balance = balance
        self.amount = amount
        self.message = f"insufficient funds, balance is {balance},amount is {amount}"
        super().__init__(self.message)
        
def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientFundsError(balance,amount)
    return balance - amount
# custom exception handling
try:
     balance =20000
     amount_to_withdraw = 25000
     new_balance = withdraw(balance,amount_to_withdraw)
except InsufficientFundsError as e:
    print("error:",{e.message})
else:
    print(f"withdrawal successful, new balance is {new_balance}")
finally:
    print("transaction completed")
#note defining a custom exception use a class and then the custom error 
    """_summary_
    class custom_exception_name(Exception):
    def init(self,parameter1,parameter2):
    super().__init__(self.message)
    self.parameter1 = parameter1
    raise custom_exception_exceptions
    def check_value(value):
    if value is < 0 or value:
    raise custom_exception_name(value)
    return value
    """
#exercise 2:define a custom exception of invalid age error and write a function that raises this exception if the age is negative
#handle this custom exception when calling the function.
# Define a custom exception for invalid age
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age cannot be negative."):
        self.age = age
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"Age is valid: {age}")


def handle_custom_exception():
    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except InvalidAgeError as e:
        print(f"InvalidAgeError: {e.message} (Age: {e.age})")
    except ValueError:
        print("Please enter a valid number.")
    finally:
        print("Code executed successfully.")
handle_custom_exception()
