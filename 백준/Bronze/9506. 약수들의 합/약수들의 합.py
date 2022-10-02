n = 0
while n != -1:
    n = int(input())
    if n == -1:
        break
    nums = []
    numSum = 0
    for i in range(1, n+1):
        if n % i == 0:
            nums.append(i)

    for i in range(len(nums) - 1):
        numSum += nums[i]

    if n == numSum:
        print("{} = " .format(n), end='')
        for i in range(len(nums) - 1):
            print(nums[i], end='')
            if i != len(nums) - 2:
                print(" + ", end='')
        print()
    else:
        print("{} is NOT perfect.".format(n))