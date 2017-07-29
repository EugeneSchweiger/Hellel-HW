import random

def generate_number_and_max_digit(r):
    rand_num = random.randint(r[0],r[1])
    print("Generated number is:", rand_num)
    max_digit = 0
    for s in str(abs(rand_num)):
        if int(s) > max_digit:
            max_digit = int(s)
    return max_digit


def max_digit_in_random_num(range1,range2):
    i=random.randint(0,1)
    if i==0:
        return generate_number_and_max_digit(range1)
    else:
        return generate_number_and_max_digit(range2)
range1 = [-((10 ** 12) - 1),-(10**11)]
range2= [(10**11),((10 ** 12) - 1)]
print("Maximal digit is:",max_digit_in_random_num(range1,range2))
