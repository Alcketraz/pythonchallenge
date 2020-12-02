import re


def allowed_characters(string):
    c = re.compile(r'[^a-zA-Z0-9.]')
    string = c.search(string)
    return not bool(string)

print(allowed_characters("ABCDedfg0975"))
print(allowed_characters("#$@!&@(!"))

Name= "ASFADCXDFabFGRIA"

x = re.search("ab", Name)
print(x)

results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

uppercase = input("Enter the string: ")

result1 = re.match('^[A-Z]+$', uppercase)
print(result1)

# OUTPUT:
# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day10.py
# True
# False
# <re.Match object; span=(9, 11), match='ab'>
# Number of length 1 to 3
# 1
# 12
# 13
# 345
# Enter the string: VEDANT
# <re.Match object; span=(0, 6), match='VEDANT'>
#
# Process finished with exit code 0
