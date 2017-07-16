import math
cathet_a=int(input("Enter first cathet lenght"))
cathet_b=int(input("Enter second cathet length"))
hyp=int(input("Ender hyprtenuse length"))
def per_sqr(a,b,c):
    per= a+b+c
    p=per/2
    sqr=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),5)
    return "Triangle square is:",sqr,"Triangle perimetre is:",per
print(per_sqr(cathet_a,cathet_b,hyp))
