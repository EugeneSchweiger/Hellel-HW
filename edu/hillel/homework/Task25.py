def factorial(p):
    if p==0:
        return 1
    else:
        return p*factorial(p-1)
power=int(input("enter factorial"))
print(factorial(22))
