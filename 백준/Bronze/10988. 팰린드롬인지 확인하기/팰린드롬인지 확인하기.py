word = input()
word2 = list(reversed(list(word)))

if word2 == list(word):
    print(1)
else:
    print(0)