number=input("Enter 3-digit number")
def int_sum(a):
    if not(len(a)==2):
        summ=int(a[:1])+int(a[1:2])+int(a[2:])
        return summ
    else:

        return None #Or print("Wrong number")
print("Sum of digits in number,you entered is:" ,int_sum(number))



