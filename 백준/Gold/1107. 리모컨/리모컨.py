import sys
input = sys.stdin.readline

n = int(input())
m = input()
broken = list(map(int, input().split()))

min_value = abs(n - 100)

for nums in range(1000000):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        elif j == len(nums) - 1:
            min_value = min(min_value, abs(int(nums) - n) + len(nums))

print(min_value)