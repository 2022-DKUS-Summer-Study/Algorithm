#5904 - moo게임
#시간복잡도 O(n)

# 입력
n = int(input())

# k값에 따른 s(k)의 길이 구하기 - 길이가 n보다 클때까지
ls = [3]

while True:
    if ls[-1] >= n:
        break
    now = ls[-1] * 2 + (len(ls)) + 3
    ls.append(now)

# k
k = len(ls) - 1


# 분할정복으로 s(k)에서 n번째 문자 찾기
def div_con(k, n):
    if k == 0:
        if n == 1:
            print('m')
        else:
            print('o')
        return
    # s(k) = s(k-1) + "moo...." + s(k-1)에서 앞의 s(k-1)이라면
    if n <= ls[k - 1]:
        div_con(k - 1, n)

    # s(k) = s(k-1) + "moo...." + s(k-1)에서 중간의 "moo...."이라면
    elif ls[k - 1] < n and n < ls[k - 1] + k + 3:
        if n - ls[k - 1] == 1:
            print('m')
        else:
            print('o')

    # s(k) = s(k-1) + "moo...." + s(k-1)에서 뒤의 s(k-1)이라면
    elif n >= ls[k - 1] + k + 3:
        div_con(k - 1, n - ls[k - 1] - k - 3)


# 분할정복 실행
div_con(k, n)

