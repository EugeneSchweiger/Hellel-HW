from time import sleep as s
class Vehicle:
    def __init__(self,fuel_consumption,maximum_speed,tank_capacity):
        self.fuel_consumption=fuel_consumption
        self.maximum_speed=maximum_speed
        self.tank_capacity=tank_capacity
        self.fuel_left=self.tank_capacity
        self.can_ride=True

    def move(self,dist):
        if self.can_ride:
            if self.fuel_consumption*(dist/100)<self.fuel_left:
                self.fuel_left-=self.fuel_consumption*(dist/100)
                print("We are moving to %s kilometers"%dist)
                s(3)
            elif self.fuel_consumption*(dist/100)==self.fuel_left:
                self.fuel_left -= self.fuel_consumption * (dist / 100)
                print("We are moving....To our last journey %s kilometers"%dist)
                self.can_ride=False
                s(3)
            else:
                print("We can't move to such long distance")
                s(3)
    def refuel(self,volume):
        if self.fuel_left!=self.tank_capacity:
            if self.fuel_left+volume<=self.tank_capacity:
                self.fuel_left+=volume
                print("We are refueleing with %s liters"%volume)
                self.can_ride=True
                s(3)
            else:
                print("To much fuel!")
                s(3)
        else:
            print("No need to refuel.Tank is full")
            s(3)
    def print_info(self):
        print('================================')
        print('fuel consumption:%s liters\\hour'%self.fuel_consumption)
        print('top speed:%s km\\h' %self.maximum_speed)
        print('tank capacity:%s liters' %self.tank_capacity)
        print("fuel left:%s litters"%self.fuel_left)
        print("Have we enough fuel?:",self.can_ride)