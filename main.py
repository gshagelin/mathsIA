import random
import numpy as np

primeList = []
def generate_prime():
    for int in range(10000, 20000, 1):
        intPrime = True
        limit = int
        for i in range(2, limit - 1, 1):
            if int % i == 0:
                #  print(str(int) + ' ' +str(i))
                intPrime = False
        if intPrime:
            primeList.append(int)

generate_prime()
q = random.choice(primeList) #secret
p = random.choice(primeList) #secret
while p == q:
    p = random.choice(primeList)

print(q)
print(p)

n = p * q #public key

lambdaP = p - 1
lambdaQ = q - 1

lambdaN = np.lcm(lambdaP, lambdaQ)    #secret



