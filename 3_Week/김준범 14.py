import heapq
import sys
def solve14(N):
    heap = []
    for _ in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
        else:
            heapq.heappush(heap, (abs(x), x))

if __name__ == '__main__':
    N = int(input())
    solve14(N)