# 11726, Silver 3, 2*n 타일링
# https://www.acmicpc.net/problem/11726
# 점화식: f(n)=f(n-1)+f(n-2)
import sys

n=int(sys.stdin.readline())
D={1:1, 2:2}

def count(n):
    if n==1:
        return D[1]
    elif n==2:
        return D[2]
    elif n>=3:
        if (n-1) not in D:
            D[n-1]=count(n-1)
        if (n-2) not in D:
            D[n-2]=count(n-2)
        return (D[n-1]+D[n-2])%10007

print(count(n))

