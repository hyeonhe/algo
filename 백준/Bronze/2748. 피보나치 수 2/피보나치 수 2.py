def fib(cache, n):
    if cache[n] != -1:
        return cache[n]
    if n == 0:
        cache[n] = n
    elif n == 1:
        cache[n] = 1
    else:
        cache[n] = fib(cache, n-1) + fib(cache, n-2)
    return cache[n]


def solve():
    n = int(input())
    cache = [-1 for i in range(n+1)]
    print(fib(cache, n))

solve()