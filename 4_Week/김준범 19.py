import random, sys
random.seed(42)
input = sys.stdin.readline
def solved19(n,k,li):
    def QuickSelect(A, k):
        s, m, l = [], [], [];
        pivot = A[random.randint(0,len(A)-1)]
        for i in A:
            if i<pivot:
                s.append(i)
            elif i == pivot:
                m.append(i)
            else:
                l.append(i)
        if len(s)>=k:
            return QuickSelect(s,k)
        elif len(s)+len(m) < k:
            return QuickSelect(l,k-len(s)-len(m))
        else:
            return pivot
    print(QuickSelect(li, k))
if __name__ == '__main__':
    n,k = map(int, input().split())
    li = list(map(int, input().split()))
    solved19(n,k,li)