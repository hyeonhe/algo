from collections import Counter
count = int(input())
my_list = []

for i in range(count):
    a = int(input)
    my_list.append(a)


def avg(my_list):
    return sum(my_list) / len(my_list)


def mid(my_list):
    my_list = sorted(my_list)
    return my_list[len(my_list) // 2]


def frequency(my_list):
    Counter(my_list)
