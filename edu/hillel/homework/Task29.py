import random
lst=[random.randint(-1,1) for i in range(11)]
print(lst)
def digits_count(lst):
    s_e_t=list(set(lst))
    count=[]
    for i in (s_e_t):
        lst.count(i)
        count.append(lst.count(i))
    if count[0]!= count[1] and count[0]!= count[2] and count[2]!= count[1]:
        print(set(lst))
        print(count)
        return count
    elif count[0]== count[1] or count[0]== count[2] or count[2]== count[1]:
        pass
digits_count(lst)

