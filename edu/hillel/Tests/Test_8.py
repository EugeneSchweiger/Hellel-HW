"""
test8
"""

import random
lst = [random.randint(1,100) for i in range(10)]
print(lst)
min=lst.index(min(lst))
max=lst.index(max(lst))
lst[min], lst[max] = lst[max], lst[min]
print(lst)