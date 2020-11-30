import math
#Q1)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lst:
    lst[i] = lst[i]+ 2

print(lst)

#Q2)


rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

#Q3)


def fibonacci(n):
    a = 0
    b = 1

    if n <=0:
        print("Invalid input!")
    elif n == 1:
        print(b)
    else:
        for i in range (2, n):
            c = a+ b
            a = b
            b = c
        print(b)


fibonacci(10)


#Q3)

for i in range(1, 10):
    print(9*i,end=" ")

#Q4)
print()
number = int(input("Enter a number: "))

if number>0:
    print("number is positive")
else:
    print("Number is negetive")

#Q5)

days = int(input("Enter the number of days: "))
years = days/365

print("Age or years: ", years)



#Q6)

print("A basic calculator: ")

num1 = int(input("enter the first number : "))
op = input("enter operator: ")
num2 = int(input("enter the second number : "))


if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)


#Q7)

x= 2

sin = math.asin(x)

print(sin)


# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day6.py
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 

# 34
# 9 18 27 36 45 54 63 72 81 
# Enter a number: 34
# number is positive
# Enter the number of days: 2356
# Age or years:  6.454794520547945
# A basic calculator: 
# enter the first number : 45
# enter operator: -
# enter the second number : 21
# 24
# -0.4667653390472964

# Process finished with exit code 0

