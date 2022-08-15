k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

# for i in range(k):
#     array.append(int(input()))

start = 0
end = min(array)
answer = 0

while True:
    