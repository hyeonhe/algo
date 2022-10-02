t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    sequence = list(range(n))

    count = 0
    while queue:
        importance = max(queue)
        while queue[0] < importance:
            queue.append(queue.pop(0))
            sequence.append(sequence.pop(0))
                
        count += 1
        if sequence[0] == m:
            break

        queue.pop(0)
        sequence.pop(0)

    print(count)