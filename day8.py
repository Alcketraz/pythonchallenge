print("Index out of bounds error:")
arr = [1,2,3,4,5,6]

try:
    print(arr[56])
except:
    print("Index not found")

print("key error:")

keys = {
        "a": 1,
        "b": 2,
        "c": 3
    }
try:
    print(keys["e"])
except KeyError:
    print("Key does not exist!")

print("Zero division error:")
try:
    print(1/0)
except:
    print("Dividing by zero is not possible")

try:
    import numpy
except:
    print("Module not found")


def division(first, second):
    try:
        result = first / second
        print(result)
    except Exception as e:
        print(e)


def multiply(first, second):
    try:
        result = first * second
        print(result)
    except Exception as e:
        print(e)


def addition(first, second):
    try:
        result = first + second
        print(result)
    except Exception as e:
        print(e)


def subtraction(first, second):
    try:
        result = first - second
        print(result)
    except Exception as e:
        print(e)


def calculation():
    try:
        first = int(input())
        second = int(input())
        division(first, second)
        multiply(first, second)
        addition(first, second)
        subtraction(first, second)
    except Exception as e:
        print("You can't put anything but integer numbers")
        calculation()



calculation()

# Output:
# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day8.py
# Index out of bounds error:
# Index not found
# key error:
# Key does not exist!
# Zero division error:
# Dividing by zero is not possible
# 34
# 22
# 1.5454545454545454
# 748
# 56
# 12
#
# Process finished with exit code 0

