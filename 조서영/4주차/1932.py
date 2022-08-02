# 1932, Silver 1, 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys

n=int(sys.stdin.readline())
tri=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if i==0:
            continue
        else:
            if j==0:
                tri[i][j]+=tri[i-1][j]
            elif j==i:
                tri[i][j]+=tri[i-1][j-1]
            else:
                tri[i][j]+=max(tri[i-1][j-1],tri[i-1][j])

print(max(tri[-1]))

