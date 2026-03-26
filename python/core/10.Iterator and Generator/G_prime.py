def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime(n):
    c = 0
    i = 0
    while c < n:
        if is_prime(i):
            yield i
            c += 1
        i += 1


p1 = prime(100)
for i in p1:
    print(i, end=" ")