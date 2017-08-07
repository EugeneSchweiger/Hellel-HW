"""
test11
"""

import pprint
import copy
lst=[[1,2,3,4,4],[2,3,4,5,8],[1,1,1,1,1],[5,5,5,5,5],[9,5,7,8,6]]

def some_fonction_that_sorts_list_columns_in_interesting_way(lst):
    lst2=copy.deepcopy(lst)
    lst3=copy.deepcopy(lst)
    for i in range(len(lst)):
        if not i%2:
            for ii in range(len(lst[i])):
                lst2[i][ii]=lst[ii][i]
            lst2[i]=sorted(lst2[i])
        else:
            for ii in range(len(lst[i])):
                lst2[i][ii]=lst[ii][i]
            lst2[i]=sorted(lst2[i],reverse=True)
    for x in range(len(lst2)):
        for xx in range(len(lst2[x])):
            lst3[x][xx]=lst2[xx][x]
    return lst3

def print_matrix(mat):
    for i in range(len(mat)):
        for x in mat[i]:
            print(x,end="\t")
        print()
print_matrix(lst)
print()
print_matrix(some_fonction_that_sorts_list_columns_in_interesting_way(lst))



