"""
test5
"""


num1=float(input("enter first any nunber"))
num2=float(input("enter second any nunber"))
target=10
if abs(num1-target)>abs(num2-target):
    print(num2,"is closer to",target)
elif abs(num2-target)>abs(num1-target):
    print(num1, "is closer to", target)
else:
    print(target,"Is equaly close to numbers")