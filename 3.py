n = 600851475143
primes = [2]

k = 3
while len(primes) < 10000:
    isprime = True
    for prime in primes:
        if k % prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(k)
    k += 2

print (primes[0:10])

for prime in primes:
    while n % prime == 0:
        n = n / prime
        print(prime)