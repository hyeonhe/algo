n = 0
while n != -1:  # n이 -1일 때까지 반복
    n = int(input())
    if n == -1:  # n이 -1이면 while문 탈출
        break
    nums = []  # n의 약수 담을 리스트
    numSum = 0   # n을 제외한 n의 약수들의 합

    # 1부터 n까지 약수 찾기
    for i in range(1, n+1):
        if n % i == 0:
            nums.append(i)

    # n을 제외한 약수 더하기
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
