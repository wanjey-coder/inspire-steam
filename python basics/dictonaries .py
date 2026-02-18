# Wanjey Gikenye
#16/2/2026
#program to show dictionaries in python


cars = {"Model" : "Audi","Make" : "Q8","Colour":"Cherry Red","Year of Manufacture":"2025"}
print(cars)

print(cars["Model"])
print(cars["Year of Manufacture"])

students = dict(Alice = 24, 
                James = 18,
                Mark = 22,
                Daisy = 19)
for key in students:
    print(key)

for val in students.values():
    print(val)
