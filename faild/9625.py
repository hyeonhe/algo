k = int(input())
ab = ['A']
for i in range(1, k+1):
    for j in range(len(ab)):
        a = ab.count('A')
        b = ab.count('B')
        # if "A" in ab and "B" not in ab:
        #     a = ab.count('A')
        #     for e in range(a):
        #         ab.remove('A')
        #         ab.append('B')

        # elif 'A' not in ab and 'B' in ab:
        #     b = ab.count('B')
        #     for e in range(b):
        #         ab.append('A')

        # elif 'A' in ab and 'B' in ab:
        #     a = ab.count('A')
        #     b = ab.count('B')
        #     for c in range(a):
        #         ab.append('B')
        #         ab.remove('A')
        #     for d in range(b):
        #         ab.append('A')

print(ab.count('A'), ab.count('B'))
