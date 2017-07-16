import math
degrees=int(input("Enter degrees value"))
def deg_rad_cos(ad): #Angle degree
    ar=ad*math.pi/180  #Angle radians
    cos=math.cos(ar)
    return round(cos,7)
print(deg_rad_cos(degrees))
print(deg_rad_cos(60))
print(deg_rad_cos(45))
print(deg_rad_cos(40))