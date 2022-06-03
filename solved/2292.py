n = int(input())

# 벌집 개수
nums_pileup = 1
# 경로 수
count = 1

while n > nums_pileup:
    nums_pileup += 6 * count
    count += 1

print(count)