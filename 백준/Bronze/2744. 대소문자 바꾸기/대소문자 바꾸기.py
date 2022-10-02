s = list(input())

for i in range(len(s)):
    if ord('A') <= ord(s[i]) < ord('a'):
        s[i] = s[i].lower()
    else:
        s[i] = s[i].upper()

print(''.join(s))