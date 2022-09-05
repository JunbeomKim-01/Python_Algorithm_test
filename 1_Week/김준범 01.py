import sys
input = sys.stdin.readline

#Comprehension 문법 이용
a = sum([int(x) for x in list(map(str,input()))[:-1]])
print(a)
