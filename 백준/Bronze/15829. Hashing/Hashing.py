import sys 

def input():
    return sys.stdin.readline().rstrip()
    
n = int(input())
word = list(input())
answer = 0
for i in range(n):
    answer += (ord(word[i]) - ord('a') + 1) * 31 ** i

print(answer)