import numpy as np

p = 67 #secret
q = 97 #secret
n = p * q #public key

lambda_n = 3 #secret

qPrime = False
while qPrime == False:
    q = np.random.randint(10000, 20000)
    if q % 2 == 0 or q % 3 == 0:
        qPrime = False
    else:
        limit = int(round(np.sqrt(q)))
        for i in range(5, limit + 1, 6):
            if n % (i+2) != 0:
                qPrime = True
                break
            else:
                qPrime = False
print(str(q) + ' ' + str(qPrime))

