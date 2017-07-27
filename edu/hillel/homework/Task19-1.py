

import random
    # int=random.randint(1, b)
int_count = int(input("enter int count(how many numbers)"))
int_range = int(input("enter int range(From 0 to....."))


def average_of_some_numbers(a,b):
    sum = 0
    int_range_range = range(a)
    for i in int_range_range:
        int = random.randint(0, int_range)
    sum = sum + int
    mid = sum / int_count
    return mid

print("The average number is:",average_of_some_numbers(int_count,int_range))
