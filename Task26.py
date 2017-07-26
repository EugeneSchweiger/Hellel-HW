def simple(rang=100):
    num=1
    lst=[1]
    for num in range(rang):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                lst.append(num)
    return lst

print(simple(200))