import random

class Vehicle:
    def __init__(self,make,color,model):
        self.make=make
        self.color=color
        self.model=model

    def printDetails(self):
        print(self.make,self.color,self.model)


class Car(Vehicle):
    def __init__(self,make,color,model,carNumber,password):
        Vehicle.__init__(self,make,color,model)
        self.carNumber=carNumber
        self.__password=password


    def printCarDetails(self):
        if self.__password==12345:
            print("Your car is :")
            self.printDetails()
            print("Thankyou for Using Car Parking")
            print("Your Car is Park at platform:",random.randint(1,9))
        else:
            print("Invalid Password")
            print("Please provide correct password:")

obj1=Car("Suzuki","Grey",2015,4,12345)
obj1.printCarDetails()

