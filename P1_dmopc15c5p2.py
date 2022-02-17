#Problem 2 - Cone Volume
# dmopc14c5p1 - Core Drill

# Simon got a new drill recently. Everyone knows that a drill is shaped like a
# right circular cone. Simon knows his drill has radius and height.
# But now he wants to calculate the volume. Write a program to help Simon!
# Input Specification
# The first line of input will have an integer  .
#
# The second line of input will have an integer  .
#
# Output Specification
# The first line of output should have the volume of Simon's drill. The output
# will be accepted if it's within an absolute or relative error of .

import math
radius = int(input())
height = int(input())

pi = (math.pi)

volume = ((pi*(r**2)*h)/3)
print(volume)
