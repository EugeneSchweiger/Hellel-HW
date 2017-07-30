import random
import sys
import string

def lst_2_str(list):
    list="".join([str(s) for s in list])
    return list

def list_index_randomizer(lst):
    choise_IDs = [i for i in range(len(lst))]
    i=0
    while i< len(lst):
        choise=int(random.choice(choise_IDs))
        lst.append(lst.pop(choise_IDs.pop(choise_IDs.index(choise))))
        i+=1
    return lst


def random_choise_from_list(lst):
    choise=random.choice(lst)
    return choise


def create_password(rang,count):
    for i in range(count):

        # small_letters=[i for i in range(97,123)]
        # big_letters=[i for i in range(65,91)]
        # numbers=[i for i in range(48,58)]
        all_posible_symbols=["_"]+list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
        password=[]
        password.append(random_choise_from_list(list(string.ascii_lowercase)))
        password.append(random_choise_from_list(list(string.ascii_uppercase)))
        password.append(random_choise_from_list(list(string.digits)))
        for i in range(abs(rang)-3):
            password.append(random_choise_from_list(all_posible_symbols))
        list_index_randomizer(password)
        lst_2_str(password)
        print(lst_2_str(password))
        i+=1

rang=int(input("Enter password length"))
count=int(input("Enter passwords count"))
create_password(rang,count)
size=(sys.getsizeof(create_password)*count)/10**6


import timeit

def test():
    return create_password(rang,count)
print(count,"Passwords generated in",timeit.timeit("test()", setup="from __main__ import test", number=1),"seconds","size:",size,"mb")

