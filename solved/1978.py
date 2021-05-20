n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(len(a)):
    divcount = 0
    for j in range(1, a[i] + 1):
        if a[i] % j == 0:
            divcount += 1
    if divcount == 2:
        count += 1

print(count)

# prime_number = []


# def prime(num):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         prime_number.append(num)


# input_list = [int(x) for x in input().split()]

# for i in range(n):
#     prime(input_list[i])

# print(len(prime_number))
