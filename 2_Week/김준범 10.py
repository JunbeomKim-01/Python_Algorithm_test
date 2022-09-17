from collections import deque
#정렬 없이 최소 값을 찾는 법?
#새로 들어온 값과 비교 , 크면 pop() -> 윈도우를 넘어가는 값을 pop()
#while()탐색이라 PyPy3로 답 체크해야합니다
def solve10(N,L,A):
    D =deque([])
    for index,val in enumerate(A):
        #큰 데이터 삭제
        while D and D[-1][0] > int(val):
            D.pop()
        D.append([int(val),int(index)])
        #인덱스 제거
        if D[0][1] <= int(index) - int(L):
            D.popleft()
        print(D[0][0], end= " ")

if __name__ == '__main__':
    N,L = map(str,input().split())
    A = list(map(str,input().split()))
    solve10(N,L,A)