def check(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


largest = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if i * j > largest:
            if check(i*j):
                largest = i * j

print(largest)