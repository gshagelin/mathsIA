import random
import numpy as np

primeList = []

M = 1882970215008405644082828404422446644402468008.0
lowestInt = int(np.ceil(np.sqrt(M)))


def generate_prime():
    for primeInt in range(lowestInt, lowestInt + 100, 1):
        intPrime = True
        primeIntFloat = float(primeInt)
        limit = int(np.ceil(np.sqrt(primeIntFloat))) + 1
        if primeInt % 2 == 0:
            intPrime = False
        else:
            for i in range(3, limit, 2):
                if primeInt % i == 0:
                    intPrime = False
                    break
            if intPrime:
                primeList.append(primeInt)


generate_prime()
q = random.choice(primeList)  # secret
p = random.choice(primeList)  # secret
print(str(p))
print(str(q))
while p == q:
    p = random.choice(primeList)


