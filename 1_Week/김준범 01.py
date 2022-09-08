import sys
input = sys.stdin.readline
def p_1(array):
    a = sum([int(x) for x in array])
    print(a)

if __name__ == '__main__':
    array =list(map(str, input().split()))
    p_1(array)