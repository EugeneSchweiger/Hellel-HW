import random

def lst_2_str(list):
    list=", ".join([str(s) for s in list])
    return list


# def digits_count(lst):
#     s_e_t=list(set(lst))
#     count=[0,0,0]
#     for i in (s_e_t):
#         lst.count(i)
#         count.append(lst.count(i))
#     if count[0]!= count[1] and count[0]!= count[2] and count[2]!= count[1]:
#         minus_one=int(count[0])
#         zero=int(count[1])
#         one=int(count[2])
#         print("-1 count is %s \n 0 count is %s \n 1 count is %s \n"%(minus_one,zero,one))
#         return count
#     elif count[0]== count[1] or count[0]== count[2] or count[2]== count[1]:
#         pass
# print(lst_2_str(lst))
# digits_count(lst)
#===================================================================================
# lover=-1
# upper=1
# rng=5
# def digits_count(lover,upper,rng):
#     lst = [random.randint(lover, upper) for i in range(rng)]
#     print(lst)
#     s_e_t = sorted(list(set(lst)))
#     count=[0]*len(s_e_t)
#     for i in range(len(s_e_t)):
#         count[i]=int(i-1),int(lst.count(int(s_e_t[i])))
#     print(count,len(count))
#     max = [(0, 0)]
#     for n in range(len(count)):
#         if max[0][1]==count[n][1]:
#                 break
#         if max[0][1] < count[n][1]:
#             max[0] = count[n]
#
#         print("The most frequant number is:",max[0][0]," and found",max[0][1],"times")

    # return count
# print(lst_2_str(lst))

# =========================================================
# lst=[random.randint(-1,1) for i in range(5)]
nums_count=int(input("enter nums count"))
def max_digits_count(nums_count=5,lower_limit=-1,upper_limit=1):
    lst = [random.randint(lower_limit, upper_limit) for i in range(nums_count)]
    print(lst_2_str(lst))
    zero = 0
    minus_one = 0
    one = 0
    for n in lst:
        if n == 0:
            zero += 1
        elif n == -1:
            minus_one += 1
        elif n == 1:
            one+=1
    if zero > one and  zero >  minus_one :
        print(" The most frequant number is:0  ",zero,"Times")
    if minus_one > zero and minus_one >one :
        print(" The most frequant number is:-1  ", minus_one,"Times")
    if one > zero and  one > minus_one :
        print(" The most frequant number is:1  ",one,"Times")
max_digits_count(nums_count)