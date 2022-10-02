num = list(map(int, input().split()))

if num[0] > 100 or num[1] > 100 or num[2] > 200 or num[3] > 200 or num[4] > 300 or num[5] > 300 or num[6] > 400 or num[7] > 400 or num[8] > 500:
    print('hacker')
elif sum(num) >= 100:
    print("draw")
else:
    print("none")