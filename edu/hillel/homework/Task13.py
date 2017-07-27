import math
cathet_a=int(input("Enter first cathet lenght"))
cathet_b=int(input("Enter second cathet length"))
def per_sqr(a,b):
    hyp=round(math.sqrt(a**2+b**2),5)
    per= a+b+hyp
    p=per/2
    sqr=round(math.sqrt(p*(p-a)*(p-b)*(p-hyp)),5)
    return sqr,per
tri_sqr,tri_per=per_sqr(cathet_a,cathet_b)
print("Triangle Square is: %s Triangle Perimetre is: %s)"
      %(tri_sqr,tri_per))