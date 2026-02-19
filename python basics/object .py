#Name : Wanjey Gikenye
#Date : 19/02/2026
#classes (objects) in python

class human:
    #first we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True

#We then create a constructor for the class/object
# the constructor will be used to create copies of this

def __init__(self, name, age):

    self.human_name = name
    self.human_age = age

def tell_story(self):
    print(f"Hello,i am {self.human_name} here is a story")
    print("There was once a bot that said hello world")


#create the objects
amani = human("Amani",17)
triza = human("Triza", 17)


#use the objects created
amani.tell_story()
print("Amani's age is : ", amani.human_age)











