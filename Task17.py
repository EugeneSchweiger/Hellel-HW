print("ax²+bx+c=0   Need to find X")
import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))


def sovle_quatro_equa(a,b,c):
    D = (b ** 2) - (4 * a * c)
    is_d_zero = (D == 0)
    is_d_lesser = (D < 0)
    is_d_grater = (D > 0)
    if is_d_lesser:
        x="No solutions in usual numbers"
        return x
    elif is_d_zero:
        x = ((-b) / 2 * a)
        return x
    elif is_d_grater:
        x1 = round(((-b + math.sqrt(D)) / 2 * a),5)
        x2 = round(((-b - math.sqrt(D)) / 2 * a),5)
        return x1,x2
print("Solution is:",sovle_quatro_equa(a, b, c))

