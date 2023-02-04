a, b = input().split()
arr = []

a = a.replace('6', '5')
b = b.replace('6', '5')

arr.append(int(a) + int(b))

a = a.replace('5', '6')
b = b.replace('5', '6')

arr.append(int(a) + int(b))

print(arr[0], arr[1])