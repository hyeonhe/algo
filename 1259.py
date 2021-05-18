while True:
    num = input()

    if int(num) == 0:
        break

    yn = 'yes'

    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            yn = 'no'
            break

    print(yn)
