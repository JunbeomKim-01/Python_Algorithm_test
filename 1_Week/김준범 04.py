import sys
input = sys.stdin.readline
def p_4(N,M):
    # 2차원 합 배열 만든는 방법
    # D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

    # D[i][j-1] = 같은 행 한 칸 뒤 합 배열의 값
    # D[i-1][j] = 같은 열 한 칸 뒤 합 배열의 값
    # D[i-1][j-1] = 대각선 합 배열의 값 ( 중복하여 값을 두 번 더했기 떄문에 빼줌)
    # A[i][j] = 현재 값
    array = [list(map(int, input().split())) for _ in range(int(N))]  # 값 배열
    sum_array = [[0] * (int(N) + 1) for _ in range(int(N) + 1)]  # 합 배열
    for i in range(1, int(N) + 1):
        for j in range(1, int(N) + 1):
            sum_array[i][j] = sum_array[i][j - 1] + sum_array[i - 1][j] - sum_array[i - 1][j - 1] + array[i - 1][j - 1]
    # 질의 값 출력
    for _ in range(int(M)):
        x1, y1, x2, y2 = map(int, input().split())
        print(sum_array[x2][y2] - sum_array[x1 - 1][y2] - sum_array[x2][y1 - 1] + sum_array[x1 - 1][y1 - 1])
if __name__ == '__main__':
    N, M = map(str, input().split())
    p_4(N,M)
