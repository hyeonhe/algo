t = int(input())

for k in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    for i in range(len(s)):
        print(s[i] * r, end='')
    print()

# t = int(input())
# string = []
# newString = []
# for i in range(t):
#     r, s = map(str, input().split())
#     r = int(r)
#     string = s
#     for j in range(len(string)):
#         for k in range(r):
#             newString.append(string[j])
#     for n in range(len(newString)):
#         print(newString[n], end='')
#     print()
#     newString = newString.
