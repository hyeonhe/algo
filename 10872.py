# def factorial(n):
#     if n == 1 or 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(int(input())))

ans = 1

n = int(input())
for i in range(n):
    if n == 1 or 0:
        ans = 1
    else:
        ans *= i + 1

print(ans)
