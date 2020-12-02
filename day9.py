from _functools import reduce

m = lambda x, y: x*y
print(m(10, 15))

lst = [1, 2, 3, 4, 5, 6, 81, 9]
print("list * 2: ")
x = list(map(lambda number: number*2, lst))
print(x)
print("Numbers divisible by 9: ")
y = list(map(lambda number1: (number1%9==0), lst))

print(y)

print("Even numbers from the list: ")

even = len(list(filter(lambda number2: number2%2==0, lst)))

print(even)

print("Fibonacci series: ")

f = lambda y: reduce(lambda x, _: x + [x[-1] + x[-2]], range(y - 2), [0, 1])

print(f(8))