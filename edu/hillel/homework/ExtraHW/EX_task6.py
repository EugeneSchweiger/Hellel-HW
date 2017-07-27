import random
"""
Попытался оптимизировать код,
чтобы он с каждым новым циклом делал всё меньше 
и меньше сравнений,удаляя ранее попавшиеся числа.
Тоже самое делал относительно списка общих чисел.
За каждый проход цикла ,из двух рандомных списков должны
были удаляться числа,которые уже появлялись в 
списке общих чисел.
Ниже огрызок кода,который уже чёрт побери,долго работает!(((
"""
# def pull_from_two_lists_simular_items(lst1, lst2 ):
#     lst_common=[0]
#     for item1 in lst1:
#         if lst_common[len(lst_common)-1] == item1:
#             pass
#         else:
#                 for item2 in lst2:
#                     lst_common = list(set(lst_common))
#                     if lst_common[len(lst_common)] == item2:
#                         lst2.remove(item2)
#                     elif item1==item2:
#                         lst_common.append(item1)
#                         lst2.remove(item2)
#     lst_common=list(set(lst_common))
#     return lst_common

"""
    Ниже код работает отлично
"""
#
# def pull_from_two_lists_simular_items(lst1, lst2 ):
#     count=0
#     lst_common=[]
#     for item1 in lst1:
#         for item2 in lst2:
#                 if item1==item2:
#                     lst_common.append(item1)
#                     count+=1
#                     lst2.remove(item2)
#
#     lst_common=list(set(lst_common))
#     return lst_common
"""
The easiest way!!!EX_task7 was an hint for this one)))
"""
def pull_from_two_lists_simular_items(lst1, lst2 ):
    return sorted(list(set(lst1) & set(lst2)))


def fill_list_with_randint(list,rng):
    for i in range(len(list)):
        list[i] = random.randint(0,rng)
    return list
list_one_size=int(input("Enter list one length"))
list_two_size=int(input("Enter list two length"))
list_one_range=int(input("Enter list one range"))
list_two_range=int(input("Enter list two range"))
list_one=[0]*list_one_size
list_two=[0]*list_two_size
list_one=fill_list_with_randint(list_one,list_one_range)
list_two=fill_list_with_randint(list_two,list_two_range)
# list_one=[2,3,3,4]
# list_two=[1,2,4,5,6]





print("List one is:",list_one)
print("List two is:",list_two)
print("Common in lists are:",pull_from_two_lists_simular_items(list_one,list_two))


