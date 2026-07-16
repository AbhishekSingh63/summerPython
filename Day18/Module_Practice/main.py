# User Defined modules

# import calculator
# from calculator import add
# from calculator import multiply, divide
# import geometry as geo

# print(add(10,5))
# print(calculator.subtract(10,5))
# print(multiply(10,5))
# print(divide(10,5))
# print(calculator.square(7))
# print(geo.area_rectangle(10,12))
# print()
# import style - 1)import calculator, 2)from calculator import add, 3)import calculator as cal, 4)from calculator import *



# Built in modules

# import math
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.pi)
# print()

# import random
# print(random.randint(1,10))
# print(random.choice(['pyhton','sql','powerBI']))
# print(random.random()) # exclusive decimals
# print()

# import datetime
# today = datetime.datetime.now()
# date = datetime.date.today()
# time=today.time()
# print(today)
# print(today.year)
# print(today.month)
# print(date)
# print(time)
# print()

# import statistics
# marks=[75,80,90,85,95]
# print(statistics.mean(marks))
# print(statistics.median(marks))
# print()

# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('for'))
# print()

# import os
# print(os.getcwd())
# print()

# import sys
# print(sys.version)
# print(sys.platform)
# print()

# to check all functions in a module
# import math
# print(dir(math))
# print(help(math.sqrt))


'''
Module Search Order -
1) Current project/script folder - Python first looks in the directory containing the script being executed.
2) Directories in the PYTHONPATH environment variable (if set) - Any custom directories you've added to PYTHONPATH are searched next.
3) Standard Library - Python searches its built-in modules, such as math, os, sys, random, etc.
4)Site-packages (Third-party libraries) - Finally, Python searches installed packages (e.g., installed using pip) in the site-packages directory. Examples: numpy, pandas, requests, flask.
'''
# import sys
# print(sys.path)

# a module executes only once
# import calculator
# import calculator
# print(calculator.add(54,23))



# Understanding the Special Variable __name__ - 
# __name__ is a built-in special variable that tells you how a Python file is being executed. It is mainly used to determine whether a file is: Executed directly, or Imported as a module into another Python file.

import math
print(math.__doc__)


# Third Party Modules - numpy, pandas, matplotlib
