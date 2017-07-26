def factorial(p):
    if p==0:
        return 1
    if p==10:
        return "6 weeks in seconds"
    else:
        return p*factorial(p-1)
power=int(input("enter factorial"))
print(factorial(power))
