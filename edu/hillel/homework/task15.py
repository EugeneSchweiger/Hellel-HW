# Так вышло что решил пойти во все тяжкие и добавить вычисление координатов
# точек пересечения двух окружностей.
import math
print("There are two circumference on plane")
circle1_cord=input("please enter 1st circle coords(Ex. 1:1)")
circle1_rad=int(input("Please,enter 1st circle radius"))
circle2_cord=input("please enter 2st circle coords(Ex. 2:2)")
circle2_rad=int(input("Please,enter 2st circle radius"))
circle1_cord=circle1_cord.split(":")
circle2_cord=circle2_cord.split(":")
print(len(circle1_cord))
def dist(a,b):
    dis=math.sqrt((int(b[0])-int(a[0]))**2+(int(b[1])-int(a[1]))**2)
    return round(dis,3)

if len(circle1_cord)==2 and len((circle2_cord))==2:
 if dist(circle2_cord,circle1_cord)==0 and circle2_rad==circle1_rad:
    print("Circles are equal")
 elif dist(circle2_cord,circle1_cord)>(circle1_rad+circle2_rad):
     print("No intersection")
 elif dist(circle2_cord,circle1_cord)==math.fabs(circle2_rad-circle1_rad):
     print("Lesser circle is inside bigger and touch each other")
 elif dist(circle2_cord, circle1_cord) < math.fabs(circle2_rad - circle1_rad):
     print("Lesser circle is inside bigger and don't touch each other")
 else:
     #Down here some mathematics from 8-th grade,newer mind,it's working properly
     P1 = circle1_cord
     P2 = circle2_cord
     rad1 = circle1_rad
     rad2 = circle2_rad
     d = dist(P1, P2)
     b = ((rad2 ** 2 - rad1 ** 2 + d ** 2) / (2 * d))
     a = d - b
     h = math.sqrt((rad1 ** 2) - (a ** 2))
     P0 = [0, 0]
     P0[0] = int(P1[0]) + (a / d) * (int(P2[0]) - int(P1[0]))
     P0[1] = int(P1[1]) + (a / d) * (int(P2[1]) - int(P1[1]))
     P3=[0,0]
     P3[0] = round(int(P0[0]) + ((int(P2[1]) - int(P1[1]) / d)) * h,1)
     P3[1] = round(int(P0[1]) - ((int(P2[0]) - int(P1[0]) / d)) * h,1)
     P4=[0,0]
     P4[0] = round(int(P0[0]) - ((int(P2[1]) - int(P1[1])) / d) * h,1)
     P4[1] = round(int(P0[1]) + ((int(P2[0]) - int(P1[0])) / d) * h,1)
     print("Circles are crossing in points %s and %s" %(P3,P4))


