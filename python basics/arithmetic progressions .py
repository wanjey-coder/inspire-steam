#Name : Wanjey Gikenye
#Date : 13/02/2026
#program to calculate arithmetic progression

#calculating the nth term

a = int(input("enter the first number:"))
n = int(input("enter the number of terms:"))
d = int(input("enter the common difference:"))

Nth_term = a + (n - 1) * d
print(f"the Nth term is : {Nth_term}")

Sn = (n/2)*((2*a) + ((n -1) * d))
print(f"the sum of the terms is: {Sn}")