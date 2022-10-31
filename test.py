from collections import deque
import sys
input = sys.stdin.readline
#새로 들어온 값과 비교 , 크면 pop() -> 윈도우를 넘어가는 값을 pop()
#while()탐색이라 PyPy3로 답 체크해야합니다
def solve10(N,L,A):
    q = deque()
    for i in range(N):
        while q and q[-1][0] > A[i]: q.pop()
        q.append((A[i], i))
        while q[0][1] <= i - L: q.popleft()
        print(q[0][0], end=' ')

N,L = map(int,input().split())
A = list(map(int,input().split()))
solve10(N,L,A)