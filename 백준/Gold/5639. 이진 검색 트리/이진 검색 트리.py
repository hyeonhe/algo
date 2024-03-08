import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def tree(first, end):
    if first > end:
        return
    
    mid = end + 1
    for i in range(first+1, end+1):
        if arr[first] < arr[i]:
            mid = i
            break
        
    tree(first+1, mid-1)
    tree(mid, end)
    print(arr[first])

tree(0, len(arr) - 1)