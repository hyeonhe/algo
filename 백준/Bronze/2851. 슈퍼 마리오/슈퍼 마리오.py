array = [int(input()) for i in range(10)]

ans = 0
for i in range(10):
  ans += array[i]
  if ans >= 100:
    a = ans - array[i]
    b = ans

    if b - 100 > 100 - a:
      ans = a
      break
      
print(ans)