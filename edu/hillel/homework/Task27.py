import random

def fill_wiz_odd(list,rang=100):
    while len(list)<(rang//2) :
        for num in range(rang):
            if num%2==0:
                continue
            list.append(num)
    return list

def lst_2_str(list):
    list=", ".join([str(s) for s in list])
    return list

lst=[]
fill_wiz_odd(lst,10000)
print(lst_2_str(lst))

def list_index_randomizer(lst):
    choise_IDs = [i for i in range(len(lst))]
    i=0
    while i< len(lst):
        choise=int(random.choice(choise_IDs))
        lst.append(lst.pop(choise_IDs.pop(choise_IDs.index(choise))))
        i+=1
    return lst


def my_shuffle(lst):
    for i in range(len(lst)):
        idx1 = random.randint(0, len(lst)-1)
        idx2 = random.randint(0, len(lst)-1)
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

def foo(lst1,lst2):
    count=0
    for i in range(len(lst1)):
        if lst1[i]==lst2[i]:
            count+=1
    return  count, "indexes on their old place"



# print(lst_2_str(my_shuffle(lst)),"shuffle",)
# print(lst_2_str(list_index_randomizer(lst)),)
print("Shuffle",foo(list(lst),list(my_shuffle(lst))))
print("IDX randomizer",foo(list(lst),list(list_index_randomizer(lst))))
