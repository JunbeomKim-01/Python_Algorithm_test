import sys
input = sys.stdin.readline

def solved17(N):
    li = list(map(int,str(N)))
    for i in li.sort(reverse=True) :
        print(i, end='')

if __name__ == '__main__':
    N = int(input())
    solved17(N)