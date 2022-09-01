#1074 - z
#시간복잡도 O(n)
# 입력
n, r, c = map(int, input().split())

# 방문한 칸 개수
count = -1


# 분할정복 구현
def div_con(n, r, c):
    global count
    #더이상 분할할 수 없다면
    if n == 0:
        count += 1
    else:
        #4등분했을 때 왼쪽 위에 위치
        if r < (2 ** n // 2) and c < (2 ** n // 2):  # 1
            div_con(n - 1, r, c)
        # 4등분했을 때 오른쪽 위에 위치
        elif r < (2 ** n // 2) and c >= (2 ** n // 2):  # 2
            count += ((2 ** n // 2) ** 2)
            div_con(n - 1, r, c - (2 ** n // 2)) # 행과 열 수정
        # 4등분했을 때 왼쪽 아래에 위치
        elif r >= (2 ** n // 2) and c < (2 ** n // 2):  # 3
            count += ((2 ** n // 2) ** 2) * 2
            div_con(n - 1, r - (2 ** n // 2), c) # 행과 열 수정
        # 4등분했을 때 오른쪽 아래에 위치
        elif r >= (2 ** n // 2) and c >= (2 ** n // 2):  # 4
            count += ((2 ** n // 2) ** 2) * 3
            div_con(n - 1, r - (2 ** n // 2), c - (2 ** n // 2)) # 행과 열 수정


# 분할정복 실행
div_con(n, r, c)

# 출력
print(count)

