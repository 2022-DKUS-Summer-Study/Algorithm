# 2758, Gold 4, 로또
# https://www.acmicpc.net/problem/2758

import sys

T=int(sys.stdin.readline())
llist=[list(map(int, sys.stdin.readline().rstrip().split())) for i in range(T)]
D={}

def combi(k,m):
    if (k,m) in D:
        return D[(k,m)]
    else:
        if k==1:
            D[(k,m)]=m
        else:
            D[(k,m)]=0
            for i in range(2**(k-1),m+1):
                D[(k,m)]+=combi(k-1,i//2)
    return D[(k,m)]

for k,m in llist:
    print(combi(k,m))


