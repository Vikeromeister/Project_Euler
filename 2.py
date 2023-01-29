m = 1
n = 2
sum = 0
while n <= 4000000:
    if n % 2 == 0:
        sum += n
    tmp = n
    n += m
    m = tmp
print (sum)