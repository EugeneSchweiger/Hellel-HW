"""
test7
"""
def fibonacci_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)


sum=0
numbers=10
for i in range(numbers):
    sum+=fibonacci_number(i)
print(sum)