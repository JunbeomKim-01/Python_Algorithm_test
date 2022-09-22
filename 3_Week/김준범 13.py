from collections import deque
def solve13(N):
    D = deque([i for i in range(1, N + 1)])
    while (len(D) > 1):
        D.popleft()
        move_num = D.popleft()
        D.append(move_num)
    print(D[0])

N = 6
solve13(N)