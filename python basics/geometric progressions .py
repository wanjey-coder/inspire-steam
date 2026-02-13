#Name : Wanjey Gikenye
#Date : 13/02/2026
#program to calculate geometric progression

n = int(input("enter number of terms: "))
a = int(input("enter the first term: "))
r = int(input("enter the common ratio: "))


import math
Tn = a*(r**(n-1))


Sn = (a*( 1 - r**n)) / (1-r)

print("The Nth term is:", Tn)
print("the sum of the terms is:", Sn)