"""
test9
"""

import random
count=int(input("Enter count of numbers"))
lst=[random.randint(-42,42)for i in range(count)]
print("Generated list",lst)
lst=[round(i/max([abs(i) for i in lst]),3) for i in lst]
print("Normalized list",lst)
