a = int(input())
b = int(input())
c = int(input())
mult = a * b * c
mult = list(str(mult))

for i in range(10):
    print(mult.count(str(i)))