from point import Point
import math
class Circle(Point):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius=radius

    def is_point_inside(self,point):
        x=abs(math.sqrt(((self.x-point.x)**2)+(self.y-point.y)**2))
        if x<=self.radius:
            return True
        else:
            return False

