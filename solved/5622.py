# s = list(input())

# time = 0
# # ord() 문자를 아스키코드 숫자로 

# # 처음 풀이
# for i in s:
#     i = ord(i)

#     # ABC
#     if 65 <= i <= 67:
#         time += 3
#     # DEF
#     elif 68 <= i <=70:
#         time += 4
#     # GHI
#     elif 71 <= i <= 73:
#         time += 5
#     # JKL
#     elif 74 <= i <= 76:
#         time += 6
#     # MNO
#     elif 77 <= i <= 79:
#         time += 7
#     # PQRS
#     elif 80 <= i <= 83:
#         time += 8
#     # TUV
#     elif 84 <= i <= 86:
#         time += 9
#     # WXYZ
#     elif 87 <= i <= 90:
#         time += 10

# print(time)


s = list(input())

alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in s:
    for j in alpha:
        if i in j:
            time += alpha.index(j) + 3

print(time)