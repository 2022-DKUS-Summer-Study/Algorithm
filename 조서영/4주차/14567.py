# 14567, Gold 5, 선수과목
# https://www.acmicpc.net/problem/14567

import sys

#과목의 수: N, 선수조건의 수: M
N,M=map(int, sys.stdin.readline().rstrip().split())
llist=[list(map(int, sys.stdin.readline().rstrip().split())) for i in range(M)]
llist=sorted(llist,key=lambda x:x[1])
llist=sorted(llist,key=lambda x:x[0])
DP=[-1]+[1 for i in range(N)]

for a,b in llist:
    if DP[b]<DP[a]+1:
        DP[b]=DP[a]+1

print(' '.join(map(str,DP[1:])))

