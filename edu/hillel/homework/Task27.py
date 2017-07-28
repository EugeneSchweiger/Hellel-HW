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
string_list=lst_2_str(lst)
random.shuffle(lst)
print(string_list)
print(lst_2_str(lst))
