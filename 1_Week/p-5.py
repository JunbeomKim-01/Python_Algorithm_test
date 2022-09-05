import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split())) + [0]
r = [0] * M
for i in range(N):
    A[i] += A[i - 1]
    r[A[i] % M] += 1
result = r[0]
for i in r:
    result += i * (i - 1) // 2
print(result)