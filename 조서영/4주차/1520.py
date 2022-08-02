# 1520, Gold3, 내리막길
# https://www.acmicpc.net/problem/1520

import sys

M,N=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited=[[-1 for _ in range(N)] for __ in range(M)]

cnt=0
def dfs(visited,i,j):
    if i==0 and j==0:
        visited[i][j]=1
        return visited[i][j]

    visited[i][j]=0
    if i-1>=0 and board[i][j]<board[i-1][j]:
        if visited[i-1][j]==-1:
            visited[i-1][j]=dfs(visited,i-1,j)
        visited[i][j]+=visited[i-1][j]
    if i+1<M and board[i][j]<board[i+1][j]:
        if visited[i+1][j]==-1:
            visited[i+1][j]=dfs(visited,i+1,j)
        visited[i][j]+=visited[i+1][j]
    if j-1>=0 and board[i][j]<board[i][j-1]:
        if visited[i][j-1]==-1:
            visited[i][j-1]=dfs(visited,i,j-1)
        visited[i][j]+=visited[i][j-1]
    if j+1<N and board[i][j]<board[i][j+1]:
        if visited[i][j+1]==-1:
            visited[i][j+1]=dfs(visited,i,j+1)
        visited[i][j]+=visited[i][j+1]

    return visited[i][j]

dfs(visited, M-1, N-1)
print(visited[M-1][N-1])
    
