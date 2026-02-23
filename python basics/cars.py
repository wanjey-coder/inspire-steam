# Wanjey Gikenye
#16/2/2026
#program to show classes in python


class Car():
    #Attributes of the car
    def __init__(self,model,make,colour,year):
        self.model = model
        self.make  = make
        self.colour = colour
        self.year = year

    #print car details
    def print_details(self,model,make,color,year):
        print(f"{make} {model} {self.colour} in colour, was manufactured in the year {year} ")



#instantiate a class object

my_car = Car("Atenza","Mazda","Red","2022")
fav_car = Car("Landcruiser","Toyota","Black","2022")

my_car.print_details("Atenza","Mazda","Red","2022")