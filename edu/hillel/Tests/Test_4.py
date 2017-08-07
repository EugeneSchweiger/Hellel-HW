"""
test4
"""
import functools
# mult=1
# while True:
#     n = input("Enter 5-digits number")
#     if len(n)==5:
#         for i in n:
#             if int(i)%2!=0:
#                 mult = mult * int(i)
#         break
#     else:
#         print("Wrong input.Enter 5!-digit number")
# print(mult)



print(functools.reduce(lambda x, y: int(x)*int(y), list(filter(lambda x:int(x)%2,input("Enter 5-digits number")))))

