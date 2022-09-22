def solve12(N,A):
    stack = []
    for i in range(N-1):
        n = i+1
        while n < N:
            if A[i] < A[n]:
                stack.append(A[i+1])
                break
            elif i == N:
                stack.append(-1)
                break
            n += 1
    stack.append(-1)
    print(stack)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))

    solve12(N,A)