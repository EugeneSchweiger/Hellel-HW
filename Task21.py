
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
    return sorted(list(set(lst3)))
print(output_all_nums_with_1_and_7())
"""
Task works correctly,however it can be divided in 3 separated methods:
1.fill_all_ints_with_1_or_7()
2.if_list_obj_contains_7(list)
3.if_list_obj_contains_1(list)
"""