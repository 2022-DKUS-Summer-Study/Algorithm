#1932 - 정수삼각형

#시간복잡도 계산 과정


#입력
n = int(input())
triangle=[]
for i in range(n):
    triangle.append(list(map(int, input().split())))

#문제유형파악 -> 중복된 작은 문제들이 존재 -> 다이나믹프로그래밍

#점화식구성 -> l : 현재계층, i : 현재층에서의 인덱스, k : 현재값
#S_l_i = max(S_l-1_i-1, S_l-1_i) + k
#만약 현재층에서의 인덱스가 0이라면, S_l_i = S_l-1_i + k
#만약 현재층에서의 인덱스가 -1이라면, S_l_i = S_l-1_i-1 + k

#dp테이블 초기화
dp=triangle

for i in range(1, n):
    for j in range(len(dp[i])):
        if j==0:
            dp[i][j]=dp[i-1][j] + dp[i][j]
        elif j==len(dp[i])-1:
            dp[i][j]=dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
#출력
print(max(dp[-1]))


