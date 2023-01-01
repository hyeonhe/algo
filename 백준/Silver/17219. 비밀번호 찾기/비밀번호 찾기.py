import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
sites = dict()

for _ in range(n):
    site, pw = input().split()
    sites[site] = pw

for _ in range(m):
    site = input()
    print(sites[site])
