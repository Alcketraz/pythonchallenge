lst1 = ["abc", "def", "ghi"]
lst2 = ["jkl", "mno", "pqr"]

merged_tuple = tuple(zip(lst1, lst2))
print("Merged tuple created form 2 lists: ")
print(merged_tuple)

for i in range(8):
    print(i)

lst3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
merged_tuple2 = tuple(zip(lst3, range(8)))
print(merged_tuple2)

sorted_list= sorted(merged_tuple2)

print(sorted_list)


lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print("Input list: ", lst4)

def only_odd(variable):
    if variable%2== 0:
        return False
    else:
        return True

print("Checking....")
print(only_odd(3))

filtered = filter(only_odd, lst4)
print("filtered list is: ", list(filtered))

# Output:
# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day11.py
# Merged tuple created form 2 lists:
# (('abc', 'jkl'), ('def', 'mno'), ('ghi', 'pqr'))
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# (('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7))
# [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]
# Input list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Checking....
# True
# filtered list is:  [1, 3, 5, 7, 9, 11, 13, 15]
#
# Process finished with exit code 0
