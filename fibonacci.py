fibonacci_cache = {}
def fibonacci_cache(n):
    # if we have cached value then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # n Compute for nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value


from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # n Compute for nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 1000):
    print(n, ':', fibonacci(n))
    # print(n, ':', fibonacci_cache(n))
