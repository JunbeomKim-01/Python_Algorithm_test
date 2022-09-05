import sys
input = sys.stdin.readline
addAll, a = map(int, input().split())
array = list(map(int, input().split()))

dp = [0] * (addAll + 1) #1번 인덱스 부터 시작

for _ in range(addAll):
    #합 배열 공식
    #S[i] = S[i-1] + A[i]
    #현재 합 배열 깂 = 이전 힙 배열 값 + 현재 값
    dp[_ + 1] = dp[_] + array[_]
    #dp[_+1] 현재 인덱스의 + 1 번 부터 채워 넣음 (1 ~ range)
for _ in range(a):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])