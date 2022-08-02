# 11053, Silver2, 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys
n=int(sys.stdin.readline())
S=list(map(int, sys.stdin.readline().rstrip().split()))
count=[1 for i in S]


for i in range(1,len(S)):
    maxN=0
    for j in range(i):
        if S[i]>S[j]: #현재 값보다 작은 값만 탐색
            if maxN<count[j]:
                maxN=count[j]
    count[i]=maxN+1

print(max(count))

