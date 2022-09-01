# 16500, Gold 5, 문자열 판별
# https://www.acmicpc.net/problem/16500

import sys

S=sys.stdin.readline().rstrip()
n=int(sys.stdin.readline())
A=[sys.stdin.readline().rstrip() for _ in range(n)]
DP=[-1 for i in S]


result=0
def dfs(i):
    if i==len(S):
        global result
        result=1
        return

    if DP[i]!=-1:
        dfs(DP[i])
        return

    for word in A:
        if S[i:i+len(word)]==word:
            DP[i]=i+len(word)
            dfs(DP[i])

    return

dfs(0)
print(result)


