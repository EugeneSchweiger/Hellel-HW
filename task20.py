import random
int_count = int(input("enter int count(how many numbers)"))
int_range = int(input("enter int range(From 0 to....."))
lst=[0]*int_count





def list_odd_even_sort(a,b):
    lst = [0] * a###creating list with length= integers count
    for i in range(a):
        lst[i] = random.randint(0, b)### filling list with random digiths
    lst_even=[0]*a
    lst_odd=[0]*a
    ###creating two lists for even and odd
    for i in range(a):### summing lists
        if lst[i]%2:
            lst_odd[i]=lst[i]
        else:
            lst_even[i]=lst[i]
    even_sum=sum(lst_even)
    odd_sum = sum(lst_odd)
    if even_sum>odd_sum:
        return lst,"even sum greater then odd for", even_sum-odd_sum
    elif even_sum<odd_sum:
        return lst,"odd sum greater then even for", odd_sum-even_sum
    else:
        return "No difference between even and odd numbers sums"

def sum(a):
    sum=0
    for i in a:
        sum += i
    return sum



print(list_odd_even_sort(int_count,int_range))