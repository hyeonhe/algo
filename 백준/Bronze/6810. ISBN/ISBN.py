isbn = '9780921418'
ans = 0
for i in range(3):
    isbn += input()

for i in range(13):
    if i % 2 == 0:
        ans += int(isbn[i])
    else:
        ans += int(isbn[i]) * 3

print(f'The 1-3-sum is {ans}')