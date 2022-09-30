import sys
input = sys.stdin.readline
def solved18(N,S):
    result = 0
    S.sort()
    for i in range(N):
        for j in range(i + 1):
            result += S[j]
    print(result)
if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    solved18(N,S)