import random
lst1=[random.randint(0,5) for i in range(5)]
lst2=[random.randint(0,5) for i in range(5)]

def list_average(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    avg=sum/len(lst)
    return avg

def avg(lst):
    return list_average(lst)

def print_something():
    print(lst1, ";average is:", avg(lst1))
    print(lst2, ";average is:", avg(lst2))

def whose_average_iz_greater(lst1, lst2):
    a=avg(lst1) > avg(lst2)
    b=avg(lst1) < avg(lst2)
    if a:
            print_something()
            print( "list_1 is greater")
    elif b:
            print_something()
            print( "list_2 is greater")
    else:
            print_something()
            print( "lists are equal")
whose_average_iz_greater(lst1,lst2)

