import sys
input = sys.stdin.readline
def solved16(N):
    arr = []
    for i in range(N):
        arr.append((int(input()), i))
    sorted_arr = sorted(arr)
    answer = []
    for i in range(N):
        answer.append(sorted_arr[i][1] - arr[i][1])
    print(max(answer) + 1)

if __name__ == '__main__':
    N = int(input())
    solved16(N)