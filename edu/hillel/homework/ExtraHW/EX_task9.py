
newlist=[[1],[[[[[[[[[[42]]]]]]]]]],[[[2,3]]],[4,[5,[6]]],7,[[[8,88]]]]
lst1=[]


def jump_in(lst):
    for i in lst:
        if type(i) != list:
            lst1.append(i)
        else:
            return jump_in(i)

def make_my_list_flat(lst):
    for i in lst:
        if type(i)!=list:
            lst1.append(i)
        else:
            jump_in(i)
    return lst1


print(make_my_list_flat(newlist))
"""
Ok,method realized, but I didn't find way to put recurtion inside "make_my_list_flat" function.
No,really,how to do that?!
"""