a = int(input())
a = '0o' + str(a)
a = int(a, 8)

print(bin(a)[2:])