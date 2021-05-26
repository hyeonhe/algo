n = int(input())

words = []
for i in range(n):
    word = input()
    words.append(word)
words = list(set(words))

for j in range(0, len(words)-1):
    first = 0
    for i in range(1, len(words)):
        if len(words[first]) > len(words[i]):
            tmp = words[first]
            words[first] = words[i]
            words[i] = tmp
        elif len(words[first]) == len(words[i]):
            if words[first] > words[i]:
                tmp = words[first]
                words[first] = words[i]
                words[i] = tmp
        first += 1

for i in range(len(words)):
    print(words[i])
