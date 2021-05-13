def factorial(num):
    if num == 1 or 0:
        return 1
    else:
        return factorial(num-1) * num
