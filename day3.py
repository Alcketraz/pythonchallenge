#Q1
dictionary1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

print("dictionary1: ", dictionary1)

dictionary2 = {
    "e": 5,
    "f": 6
}

print("dictionary2: ", dictionary2)

dictionary1.update(dictionary2)

print("Merged dictionary is:")

print(dictionary1)

#Q2

del dictionary1['f']

print("Deleting last key: ")

print(dictionary1)

#Q3

continents = ["Asia", "Europe", "America"]
countries = ["India", "England", "USA"]

dictionary3 = dict(zip(continents, countries))

print("mapping 2 lists into dictionary: ")
print(dictionary3)

#Q4

colors1 = {"red", "blue", "yellow", "green", "pink", "orange", "black"}

print("colors1= ", colors1)

print("length of set 'colors':")
print(len(colors1))

#Q5

colors2 = {"violet", "pink", "green", "cyan", "grey"}
print("colors2= ", colors2)

colors1.difference_update(colors2)
print("Updated 'colors1' set: ")

print(colors1)


# Output:
# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day3.py
# dictionary1:  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dictionary2:  {'e': 5, 'f': 6}
# Merged dictionary is:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# Deleting last key:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# mapping 2 lists into dictionary:
# {'Asia': 'India', 'Europe': 'England', 'America': 'USA'}
# colors1=  {'blue', 'black', 'pink', 'red', 'orange', 'yellow', 'green'}
# length of set 'colors':
# 7
# colors2=  {'grey', 'pink', 'violet', 'cyan', 'green'}
# Updated 'colors1' set:
# {'blue', 'black', 'red', 'orange', 'yellow'}
#
# Process finished with exit code 0
#
#
