#1010 - 다리놓기

#시간복잡도 계산 과정


import math
#입력
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    #출력
    print(math.factorial(m)//(math.factorial(n)*(math.factorial(m-n))))


