number=int(input("Enter 3-digit number"))
def int_sum(a):
    int1=a%10
    int2=(a%100)//10
    int3=a//100
    sum=int1+int2+int3
    return sum
print("Sum of digits in number,you entered is:" ,int_sum(number))



