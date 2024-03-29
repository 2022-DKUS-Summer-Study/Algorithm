#
# # 투 포인터를 위한 필드값 선어
# s, e = 0, n - 1  # 시작 및 끝값
# sum = 0  # 용액의 합을 내기위한 값
# liquid1, liquid2 = liquid[s],liquid[e]
# tmp_min =liquid1 + liquid2  # 정렬된 값의 덧셈으로 먼저 큰 범위의 초기값 구하기
#
#
# while s < e:
#     # 정렬이 된 리스트에서 각각의 값을 가져와 더해준다
#     sum = liquid[s] + liquid[e]
#
#     # 만약 sum의 절댓값이 임시 최소값 보다 작다면 대체
#     if abs(sum) <= abs (tmp_min): #sum의 값이 0보다 작을 경우의 비교를 위해 abs를 통해 절댓값 끼리의 비교
#         tmp_min = abs(sum)
#         liquid1, liquid2 = liquid[s], liquid[e]  #만약 값이 변동이 된다면 주어진 liquid 값 교체
#         if tmp_min == 0: # 바뀐 값이 0이된다면 반복문 중지
#             break
#
#     if sum < 0: # 만약 sum이 0보다 작다면 음수쪽으로 정렬된 부분이 더 크다는 의미이므로 s의 시점을 한 칸 이동
#         s += 1
#     else: # sum이 0보다 크거나 0과 같을 경우 0에 근접해야하는 경우가 목적이므로 e의 지점을 이동
#         e -= 1
''''
문제의 경우 투 포인터로 접근하라 하였다. 따라서 처음에 정렬이 된 리스트를 입력 받고 진행한다
문제의 요구하는 답은 0 혹은 0에 근접한 값을 만드는 두 용액을 구하는 것이다. 따라서 이것을 목표로 진행을 하였다.
처음에는 문제의 답을 도출하는 과정에서 투포인터의 진행을 위한 지점의 이동을 어떤식으로 구현해야하나 고민을 했었다.
하지만 문제의 답이 0을 만드는 것에 목표를 한다는 것에 초점을 두었고 음수의 경우에는 시작점을 이동
양수일 경우 끝점을 이동하는 식으로 반복을 진행하였다. 또한 s가 e보다 작은 경우에만 진행을 하는 반복문으로 시작을 하였다.

처음 tmp_min의 경우 값을 1e9로 가장 큰값을 주고 시작을 했다. 이 경우 비교를 하면서 바로 수가 사라질 것이라 생각을 하였기 때문이다.
하지만 지속적으로 오답의 경우가 나와 찾아보니 test case로 각각의 수가 1e9가 나오게 되는 경우에는 내 답이 틀린 답이 되기에 tmp_min의 값을
제대로 지정해줘야했다. 따라서 고민을 하다가 찾아보니 답은 간단하게 tmp_min의 값을 정렬이 된 리스트에서 가장 큰 값과 작은 값의 합으로 표현하라
하였기에 이 부분을 참고하게 되었다.
'''

n = int(input())
liquid = sorted(list(map(int, input().split())))
liquid1, liquid2 = liquid[0], liquid[len(liquid) - 1]

for i in range(len(liquid)):
    s = i + 1
    e = n - 1
    sum = liquid1 + liquid2
    while s <= e:
        mid = (s + e) // 2
        tmp = liquid[i] + liquid[mid]
        if abs(tmp) < abs(sum):
            sum, liquid1, liquid2 = tmp, liquid[s], liquid[mid]
        if sum < 0:
            s = mid + 1
        else:
            e = mid - 1

print(liquid1, liquid2)

