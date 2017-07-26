import random

def max_digit_in_random_num(range):
    range=((10**12)-1)
    rand_num=random.randint(-range,range)
    print("Generated number is:",rand_num)
    max_digit=0
    for s in str(abs(rand_num)):
        if int(s)>max_digit:
            max_digit=int(s)
    return max_digit
range = ((10 ** 12) - 1)
print("Maximal digit is:",max_digit_in_random_num(range))
"""
There is only one thing to add:
range should be between -(10^12...10^11):(10^11...10^12)
"""