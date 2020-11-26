# Q1)

lst1 = []

n = int(input("Number of elements: "))
for i in range(0, n):
    element = int(input("enter the element: "))
    lst1.append(element)


print(lst1)

d = int(input("Enter the element which you want to delete: "))

for i in lst1:
    if d == i:
        lst1.remove(d)
        print("element deleted successfully")
        break
else:
    print("element does not exist")

print(lst1)

maximum = max(lst1)
print("Maximum element is: ", maximum)

minimum = min(lst1)
print("Minimum element is: ", minimum)


#Q2)

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

rev = tup[::-1]
print(rev)

#Q3)
tup1 = (100, 101, 102, 103, 104, 105)
print("Tuple: ", tup1)

lst2 = list(tup1)
print("Converting tuple to list")
print(lst2)

# OUTPUT:
#
# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day4.py
# Number of elements: 5
# enter the element: 12
# enter the element: 45
# enter the element: 23
# enter the element: 67
# enter the element: 34
# [12, 45, 23, 67, 34]
# Enter the element which you want to delete: 67
# element deleted successfully
# [12, 45, 23, 34]
# Maximum element is:  45
# Minimum element is:  12
# (9, 8, 7, 6, 5, 4, 3, 2, 1)
# Tuple:  (100, 101, 102, 103, 104, 105)
# Converting tuple to list
# [100, 101, 102, 103, 104, 105]
#
# Process finished with exit code 0
#
