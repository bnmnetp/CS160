import decimal
numHashes = decimal.Decimal(float(2 ** 128))
current = numHashes-1
i = 0
done = False
notp = decimal.Decimal(1.0)
while not done:

    notp =  notp * current/numHashes
    if 1 - notp >= 0.01:
        print("probability is 1% after {} tries".format(i))
        done = True
    if i % 10000000 == 0:
        print("After {} tries the probability is {}".format(i, 1-notp))
    i += 1
    current -= 1