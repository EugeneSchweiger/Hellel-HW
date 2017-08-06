"""
test12
"""
import pprint
import random
tasks = 15
lst_1=[i for i in range(2,10)]
lst_2=[i for i in range(2,10)]
def mult_tasks(lst_1,lst_2):
    count=0
    lst_of_tasks = []
    while count<15:
        a = random.choice(lst_1)
        b = random.choice(lst_2)
        multiply1 = ("%d*%d" % (a, b))
        multiply2 = ("%d*%d" % (b, a))
        if multiply1 in lst_of_tasks:
            continue
        elif multiply2 in lst_of_tasks:
            continue
        else:
            lst_of_tasks.append(multiply1)
        count += 1
    return lst_of_tasks
pprint.pprint(mult_tasks(lst_1,lst_2))