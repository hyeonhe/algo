original_num = int(input())
new_num = original_num
count = 0
result = 0

while True:
    ten = new_num // 10
    one = new_num % 10
    result = ten + one
    new_num = one * 10 + result % 10
    count += 1
    if original_num == new_num:
        break

print(count)
