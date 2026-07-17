'''Different Methods of Importing Package'''
import calculator # when modules are imported in __init__.py

import calculator.advanced # import a particular module from package directly

from calculator import advanced

from calculator.advanced import square

from calculator.arithmetic import *


'''Absolute Import - Done directly in main.py file, no module import in __init__.py'''
from calculator.arithmetic import multiply

print(calculator.addition(10,20))