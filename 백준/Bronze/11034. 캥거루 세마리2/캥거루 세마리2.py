try:
    while True:
        a, b, c = map(int, input().split())
        print(max(b-a, c-b) - 1)
except:
    exit(0)