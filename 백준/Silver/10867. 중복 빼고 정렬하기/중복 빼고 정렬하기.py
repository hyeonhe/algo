n = int(input())
array = set(map(int, input().split()))
array = list(array)
array.sort()

print(' '.join(map(str, array)))