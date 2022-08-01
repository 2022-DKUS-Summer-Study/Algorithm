#11726 - 2*n 타일링

#시간복잡도 계산 과정


# 입력
n = int(input())

# memoization
m = [0] * (n + 1)

# dp
for i in range(1, n + 1):
    if i == 1 or i == 2:
        m[i] = i
    else:
        m[i] = m[i - 1] + m[i - 2]

# 출력
print(m[n] % 10007)

