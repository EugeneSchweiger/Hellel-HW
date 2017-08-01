def factorial(p):
    if p==0:
        return 1
    else:
        return p*factorial(p-1)


def PASKAL_triangle(n):
    for i in range(n):
        for j in range(n+1):
            print(int(factorial(n)/(factorial(j)*factorial(n-j))), end="  ")
        n-=1
        print()
    if n==0:
        print(1)
lines=int(input("Q'ty of lines"))
print(PASKAL_triangle(lines))
"""
How to move text to the center??????????
"""
