# An exception is a kind of error that crashes the program, so use the try except to print out an appropriate error message instead of crashing the whole program.

try:
    age = int(input("What is your age? "))
    income = 20000
    risk = income/age
    print("Your age is", age)

except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("You didn't enter a number.")