# word = input()
# bool = True
# for i in range(len(word) // 2):
#     if word[i] == word[len(word) - 1 - i]:
#         continue
#     else:
#         bool = False
#         break

# print(int(bool))

word = input()
word2 = list(reversed(list(word)))

if word2 == list(word):
    print(1)
else:
    print(0)
