from time import sleep as s
class Vehicle:
    """
    fc-fuel consumption
    ms-maximum speed
    tc-tank capacity
    """


    def __init__(self,fc,ms,tc):
        self.fc=fc
        self.ms=ms
        self.tc=tc
        self.fuel_left=self.tc
        self.can_ride=True

    def move(self,dist):
        if self.can_ride:
            if self.fc*(dist/100)<self.fuel_left:
                self.fuel_left-=self.fc*(dist/100)
                print("We are move to %s kilometers"%dist)
                s(3)
            elif self.fc*(dist/100)==self.fuel_left:
                self.fuel_left -= self.fc * (dist / 100)
                print("We are move....To our last journey %s kilometers"%dist)
                self.can_ride=False
                s(3)
            else:
                print("We can't move to such long distance")
                s(3)
    def refuel(self,volume):
        if self.fuel_left!=self.tc:
            if self.fuel_left+volume<=self.tc:
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
        print('fuel consumption:%s liters\\hour'%self.fc)
        print('top speed:%s km\\h' %self.ms)
        print('tank capacity:%s liters' %self.tc)
        print("fuel left:%s litters"%self.fuel_left)
        print("Can move?:",self.can_ride)