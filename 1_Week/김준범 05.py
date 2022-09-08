import sys
input = sys.stdin.readline
def p_5(N,M,A,r):
    # N이 10^6이기 때문에 이중 for문은 불가능하는 것을 알 수 있다.
    # SUM(i,j) % M = 0 => SUM(1,j) - SUM(1,i-1) % M =0
    # => SUM(i,j) % M = SUM(1,i-1) % M
    # SUM(i,j) = 단순 구간 합 => O(n)
    # * 모듈러스 배열을 만드는 것 *
    for i in range(N):
        A[i] += A[i - 1]  # 구간 합 배열
        r[A[i] % M] += 1  # 구간 합 배열의 값의 모듈러스 값
    result = r[0]  # result의 초기값은 M의 배수의 요소 수
    for i in r:  # (같은 개수)C(2) C : Combination
        result += i * (i - 1) // 2
    print(result)

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split())) + [0]
    r = [0] * M #모듈러스의 결과 배열 (0~M-1)
    p_5(N,M,A,r)
    #기본적인 누적합에 모듈러스 분배법칙을 적용한 문제