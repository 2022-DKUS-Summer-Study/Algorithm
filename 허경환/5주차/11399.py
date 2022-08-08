#11399 - ATM
#시간복잡도 계산 과정


from itertools import accumulate
#입력
n = int(input())
p = list(map(int, input().split()))

#그리디 알고리즘
#시간이 덜 걸리는 사람부터 필요 시간 구하기
#정당성 검토 : 시간이 많이 걸리는 사람이 앞 순서이면 많은 시간을 다수가 대기해야함


#정렬
p.sort()

#누적합
acc_p = list(accumulate(p))

#출력
print(sum(acc_p))

