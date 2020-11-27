#Q1)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def division(a, b):
    return a/b


def multiply(a, b):
    return a*b


print("addition of 2 numbers is: ", addition(number1, number2))
print("subtraction of 2 numbers is: ", subtraction(number1, number2))
print("division of 2 numbers is: ", division(number1, number2))
print("multiplication of 2 numbers is: ", multiply(number1, number2))


#Q2)


def covid(temp=98):
    name = input("Enter the patient name: ")
    print("name= ", name)
    print("temperature= ", temp)


covid()

# OUTPUT:
# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day5.py
# Enter the first number: 10
# Enter the second number: 2
# addition of 2 numbers is:  12
# subtraction of 2 numbers is:  8
# division of 2 numbers is:  5.0
# multiplication of 2 numbers is:  20
# Enter the patient name: Vedant
# name=  Vedant
# temperature=  98
#
# Process finished with exit code 0
