t = int(input())
n = list(map(int, input().split()))

# print(type(n[1]))
for i in n:
    lst = []
    for j in range(1, i):
        if i % j == 0:
            lst.append(j)

    result = sum(lst)
    if result == i:
        print('Perfect') 
    elif result > i:
        print('Abundant')
    else:
        print('Deficient')