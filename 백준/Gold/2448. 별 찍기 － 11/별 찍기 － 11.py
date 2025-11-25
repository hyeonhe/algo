import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

arr = [[" "] * 2 * n for _ in range(n)]

def recursion(i, j, size):
    if size == 3:
        arr[i][j] = "*"
        arr[i + 1][j - 1] = arr[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            arr[i + 2][j + k] = "*"
    else:
        n_size = size // 2
        recursion(i, j , n_size)
        recursion(i + n_size, j - n_size, n_size)
        recursion(i + n_size, j + n_size, n_size)
            
recursion(0, n - 1, n)

for line in arr:
    print("".join(line))