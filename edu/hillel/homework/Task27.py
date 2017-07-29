import random

def fill_wiz_odd(list,rang=100):
    while len(list)<(rang/2) :
        for num in range(rang):
            if num%2==0:
                continue
            list.append(num)
    return list

def lst_2_str(list):
    list=", ".join([str(s) for s in list])
    return list

lst=[]
fill_wiz_odd(lst)
print(lst)

def foo(lst):
    choise_IDs = [i for i in range(len(lst))]
    lst2=[]
    i=0
    while i< len(lst):
        choise=int(random.choice(choise_IDs))
        lst2.append(lst[choise_IDs.pop(choise_IDs.index(choise))])
        i+=1
    return lst2

print(foo(lst))
