from typing import Counter

word = input()
word = word.upper()
a = Counter(word).most_common(2)

if len(word) == 1:
    print(word)
elif a[0][1] == a[1][1]:
    print('?')
else:
    print(a[0][0])