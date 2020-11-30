from day7module import list_of_numbers
import pandas as pd
import random as rd

import sys
print(list_of_numbers)

list_of_numbers[3] = 89

print(list_of_numbers)

a = rd.randint(1, 100)

print(a)

import sys

for p in sys.path:
    print(p)


# C:\python37\python.exe C:/Users/Vedant/PycharmProjects/pythonInternship/day7.py
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 89, 5, 6, 7, 8, 9, 10]
# 82
# C:\Users\Vedant\PycharmProjects\pythonInternship
# C:\Users\Vedant\PycharmProjects\pythonInternship
# C:\python37\python37.zip
# C:\python37\DLLs
# C:\python37\lib
# C:\python37
# C:\Users\Vedant\AppData\Roaming\Python\Python37\site-packages
# C:\python37\lib\site-packages
# C:\python37\lib\site-packages\win32
# C:\python37\lib\site-packages\win32\lib
# C:\python37\lib\site-packages\Pythonwin
#
# Process finished with exit code 0

# C:\WINDOWS\system32>pip uninstall pandas
# Found existing installation: pandas 1.0.5
# Uninstalling pandas-1.0.5:
#   Would remove:
#     c:\python37\lib\site-packages\pandas-1.0.5.dist-info\*
#     c:\python37\lib\site-packages\pandas\*
# Proceed (y/n)? y
#   Successfully uninstalled pandas-1.0.5
#
# C:\WINDOWS\system32>pip install pandas
# Collecting pandas
#   Downloading pandas-1.1.4-cp37-cp37m-win_amd64.whl (8.7 MB)
#      |████████████████████████████████| 8.7 MB 939 kB/s
# Requirement already satisfied: python-dateutil>=2.7.3 in c:\python37\lib\site-packages (from pandas) (2.8.1)
# Requirement already satisfied: pytz>=2017.2 in c:\python37\lib\site-packages (from pandas) (2020.1)
# Requirement already satisfied: numpy>=1.15.4 in c:\python37\lib\site-packages (from pandas) (1.19.0)
# Requirement already satisfied: six>=1.5 in c:\users\vedant\appdata\roaming\python\python37\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)
# Installing collected packages: pandas
# Successfully installed pandas-1.1.4
# WARNING: You are using pip version 20.1.1; however, version 20.2.4 is available.
# You should consider upgrading via the 'c:\python37\python.exe -m pip install --upgrade pip' command.
#
# C:\WINDOWS\system32>


