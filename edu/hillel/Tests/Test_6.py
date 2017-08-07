"""
test6
"""

import random
primes = lambda rang: [num for num in range(2, rang) if not 0 in map(lambda z: num % z, range(2,(num//2)+1))]
print([random.choice(list(map(int, primes(10**3)))) for i in range(10)])