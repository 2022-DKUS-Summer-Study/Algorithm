# 1010, Silver 5, 다리 놓기
# https://www.acmicpc.net/problem/1010

import sys
from itertools import combinations
T=int(sys.stdin.readline())
llist=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(T)]
DP={}

def combi(n,k):
    if (n,k) in DP:
        return DP[(n,k)]
    else:
        if n==k:
            DP[(n,k)]=1
            return DP[(n,k)]
        elif k==1:
            DP[(n,k)]=n
            return DP[(n,k)]
        elif n-1>=1 and k-1>=1:
            DP[(n,k)]=combi(n-1,k)+combi(n-1,k-1)
            return DP[(n,k)]

for l in llist:
    big=max(l)
    small=min(l)
    print(combi(big, small))

