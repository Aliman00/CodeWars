def is_prime(n):
    return n > 1 and all(n % i for i in xrange(2, int(n ** 0.5) + 1))


def circular_prime(n):
    num = str(n) * 2
    length = len(num) / 2
    for a in xrange(length):
        if not is_prime(int(num[a:a + length])):
            return False
    return True
