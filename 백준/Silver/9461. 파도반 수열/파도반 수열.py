n = int(input())

num_list = [0, 1, 1]

for i in range(3, 101):
    num_list.append(num_list[i-3] + num_list[i-2])

for i in range(n):
    k = int(input())
    print(num_list[k])