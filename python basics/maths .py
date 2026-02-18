#Name : Wanjey Gikenye
#Date : 13/02/2026
#program to do mathematical operations
number = -16.79

import math
print(abs(number))

angle_degrees = 60
angle_radians = math.radians(angle_degrees)


x=1
y= math.degrees(x)

from tabulate import tabulate
cos_val = (math.cos(angle_radians))
sin_val = (math.sin(angle_radians))
tan_val = (math.tan(angle_radians))

data = [[angle_degrees, cos_val, sin_val, tan_val]]

print(tabulate(data,headers=["angle","cos","sin","tan"],tablefmt="grid"))



print(min(3,4))
print(max(13,46))

print(math.sqrt(144))

print(25**2)