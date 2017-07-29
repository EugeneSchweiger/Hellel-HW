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
print(lst_2_str(lst))

def list_index_randomizer(lst):
    choise_IDs = [i for i in range(len(lst))]
    i=0
    while i< len(lst):
        choise=int(random.choice(choise_IDs))
        lst.append(lst.pop(choise_IDs.pop(choise_IDs.index(choise))))
        i+=1
    return lst

print(lst_2_str(list_index_randomizer(lst)))
