import sys
input = sys.stdin.readline

a = sum([int(x) for x in list(map(str,input()))[:-1]])
print(a)
