primes = [2]

k = 3
while len(primes) < 10002:
    isprime = True
    for prime in primes:
        if k % prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(k)
    k += 2

print (primes[10000])