def lst_2_str(list):
    list=", ".join([str(s) for s in list])
    return list

"""
Hard way
"""
def output_all_nums_with_1_and_7():
    n = 1000
    lst1 = []
    count = 0
    lst2 = []
    lst3 = []
    for i in range(n):
        for char in str(i):
            if char=="1" or char=="7":
                lst1.append(i)
                count+=1
    for item_1 in lst1:
        for char_1 in str(item_1):
            if  char_1=="7":
                lst2.append(item_1)
    for item_2 in lst2:
        for char_2 in str(item_2):
            if  char_2=="1":
                lst3.append(item_2)
    return lst_2_str(sorted(list(set(lst3))))
print(output_all_nums_with_1_and_7())

"""
Easy way
"""

def output_all_nums_with_1_and_7(number_1, number_2,rng=1000):
    lst = []
    for i in range(rng):
        if str(number_1) in str(i) and str(number_2) in str(i):
            lst.append(i)
    return lst_2_str(lst)

print(output_all_nums_with_1_and_7(1,7,1000))