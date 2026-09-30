class ValueTooLowError(Exception) : 
    pass 

try : 
    number = int(input("Enter a number : "))
    # variable = 10/0
    if number < 5 : 
        raise ValueTooLowError("Your value is low as input")
except ZeroDivisionError as e: 
    print("You got an error ->",e)
except ValueError as error_message : 
    print("Invalid form of input",error_message)
except ValueTooLowError as v : 
    print(v)
except : 
    print("Invalid syntax")


