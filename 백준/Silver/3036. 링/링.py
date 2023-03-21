def gcd(x, y):
    if y == 0:
      return x
    return gcd(y, x % y)
  
n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    num = gcd(arr[0], arr[i])
    print(f'{arr[0] // num}/{arr[i] // num}')