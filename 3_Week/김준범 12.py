from collections import deque
def solve12(N,A):
    stack = deque()
    ls = [-1] * N

    for i in range(N):
        while stack and (stack[-1][0] < A[i]):
            tmp, index = stack.pop()
            ls[index] = A[i]
        stack.append([A[i], i])
    print(*ls)# 공백기준 원소만 나열

if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    solve12(N,A)