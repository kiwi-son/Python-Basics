"""
Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
"""
num=[1,2,3,4,5]
square=lambda x: x*x
print(list(map(square,num)))

"""
Import the math module and use it to:

Find the square root of 144
Calculate sin(90°) (hint: use math.radians())
"""

import math
print(math.sqrt(144))
print(math.sin(math.radians(90)))

