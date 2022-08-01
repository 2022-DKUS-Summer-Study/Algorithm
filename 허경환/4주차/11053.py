#11053 - 가장 긴 증가하는 부분수열

#시간복잡도 계산 과정


#입력
n = int(input())
seq=list(map(int, input().split()))

#메모이제이션 - dp테이블 생성 : 자신을 포함하여 만들 수 있는 부분 수열 길이 저장
table=[0]*n

#bottom-up
for i in range(n):
    for j in range(i):
        if seq[i]>seq[j] and table[i]<table[j]:
            table[i]=table[j]
    table[i]+=1

#출력
print(max(dp))


