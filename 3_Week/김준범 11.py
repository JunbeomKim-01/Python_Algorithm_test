def solve11(N):
    stack = []
    result = []
    cur = 1
    excep = False
    for i in range(N):
        n = int(input())
        while cur <= n:
            stack.append(cur)
            result.append('+')
            cur += 1
        if stack[-1] == n:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            excep = True
            break
    if not excep:
        for i in result:
            print(i)

if __name__ == '__main__':
    N = int(input())
    solve11(N)