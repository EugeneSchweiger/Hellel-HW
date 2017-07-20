print("ax²+bx+c=0   Need to find X")
import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
D=(b**2)-(4*a*c)
is_D_zero=(D==0)
is_D_lesser=(D<0)
is_D_grater=(D>0)

if is_D_lesser:
    print("No solutions in usual numbers")
elif is_D_zero:
    x = ((-b) / 2 * a)
    print(x)
elif is_D_grater:
    x1 = round(((-b + math.sqrt(D)) / 2 * a),5)
    x2 = round(((-b - math.sqrt(D)) / 2 * a),5)
    print(x1, x2)

# def is_D_zero(val):
#     return val==0
# if is_D_zero(D):
#     print("Only 1 x")
#
# def is_D_lesser(val):
#     return val==0
# if is_D_lesser(D):
#     print("No solutions in usual numbers")
#
# def is_D_greater(val):
#     return val==0
# if is_D_greater(D):
#     print("Two x's")
#
#
# if D==0:
#         x = ((-b) / 2 * a)
#         print(x)
# elif D > 0:
#         x1 = (-b + math.sqrt(D)) / 2 * a
#         x2 = (-b - math.sqrt(D)) / 2 * a
#         print(x1, x2)
# else: print("No solutions in usual numbers")




