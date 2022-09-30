import sys
input = sys.stdin.readline
def solved20(N):
    ls = []
    for _ in range(N):
        ls.append(int(input()))
    ls.sort()
    for i in ls:
        print(i)

if __name__ == '__main__':
    N = int(input())
    solved20(N)