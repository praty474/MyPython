# modules 
# dividing the large chunk of code into smaller related chunk each file is known as module
# any py file is module
# module has reuseable code

import constants

print(constants.PI)

# if you want to import only one item from file 

from constants import GRAVITY

print(GRAVITY)

import math

print(math.sqrt(25))

# package is collection of related modules

from maths.arith import add

add()

# collection of related package make library

# pip 