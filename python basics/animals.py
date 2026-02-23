# Wanjey Gikenye
#16/2/2026
#program to illustrate inheritance in python

class Animal():

    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animals weighs {weight} kgs")

    def eats(self,food):
        print("The animal eats {food}")   

class Dog(animal):
    def __init__(self,colour,height,breed):
        super().__init__(species,weight,food)
        self.weight = weight
        self.breed = breed  


class horse(animal):
    def __init__(self,species,weight,food):

        