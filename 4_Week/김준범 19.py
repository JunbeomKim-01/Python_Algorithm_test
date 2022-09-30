import sys
input = sys.stdin.readline
def solved19(N,K,A):
    A.sort()
    print(A[K - 1])

if __name__ == '__main__':
    N,K =map(int,input().split())
    A = list(map(int,input()))
    solved19(N,K,A)