
def output_all_nums_with_1_and_7():
    n = 1000
    lst = []
    count = 0
    lst2=[]
    lst3 = []
    for i in range(n):
        for char in str(i):
            if char=="1" or char=="7":
                lst.append(i)
                count+=1
    for char_2 in lst:
        for char_1 in str(char_2):
            if  char_1=="7":
                lst2.append(char_2)
    for char_4 in lst2:
        for char_3 in str(char_4):
            if  char_3=="1":
                lst3.append(char_4)
        ###
    lst3=list(set(lst3))
    lst3.sort()
    return lst3
print(output_all_nums_with_1_and_7())
"""
Task works correctly,however it can be divided in 3 separated methods:
1.fill_all_ints_with_1_or_7()
2.if_list_obj_contains_7(list)
3.if_list_obj_contains_1(list)
"""