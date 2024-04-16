#we will create a simple class in python

#class Car:
    #model = "Volvo"
    #color = "Red"

#car = Car()
#car.model = "Volvo"
#car.color = "Red"


#print(car.model)
#print(car.color)


# THE __init __ FUNCTION.
# every class in python has an inbuilt function called init in other programming languages the constructor

#class Car:
    #def __init__(self, model, color, yom, price):
        #self.model = model
        #self.color = color
        #self.yom = yom
        #self.price = price

#creating a new instance of a car1
#car1 = Car("Benz","White","2019","ksh.5,300,000")

#accessing the attributes.
#print(car1.model)
#print(car1.color)
#print(car1.yom)
#print(car1.price)

#creating a new instance of car2
#car2 = Car("Bentley", "Black", "2020", "ksh.15,000,000")

#accessing the attributes.
#print(car2.model)
#print(car2.color)
#print(car2.yom)
#print(car2.price)

#INIT FUNCTION AND CLASS METHODS.

#lets define a class car
class Car:
    def __init__(self, model,color):
        self.model = model
        self.color = color

        #let's define a method (class function) 
        def displayCar(self):
            print(self.model)
            print(self.color)

#let's start using the class
car1 =Car("Tesla", "Red")
#car1.displayCar()
print(car1.model)
print(car1.color)




