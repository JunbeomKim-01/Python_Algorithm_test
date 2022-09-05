import sys
input = sys.stdin.readline
addAll, a = map(int, input().split())
array = list(map(int, input().split()))
dp = [0] * (addAll + 1)
for _ in range(addAll):
    dp[_ + 1] = dp[_] + array[_]
for _ in range(a):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])