from os import sep


n = int(input())
word = []

one = []
ten = []
list100 = []
list1000 = []
list10_000 = []
list100_000 = []
list1_000_000 = []
list10_000_000 = []

for i in range(n):
    a = input()
    word.append(a)


def seperate(list, k):
    try:
        for i in range(len(word)):
            list.append(word[i][-k])
    except IndexError:
        pass


seperate(one, 1)
seperate(ten, 2)
seperate(list100, 3)
seperate(list1000, 4)
seperate(list10_000, 5)
seperate(list100_000, 6)
seperate(list1_000_000, 7)
seperate(list10_000_000, 8)
print(word)
print(one)
print(list10_000_000)
