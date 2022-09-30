import sys
input = sys.stdin.readline
def solved18(N,S):
    result = 0
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        lesser_arr, equal_arr, greater_arr = [], [], []
        for num in arr:
            if num < pivot:
                lesser_arr.append(num)
            elif num > pivot:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
        return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
    S = quick_sort(S)
    for i in range(N):
        for j in range(i + 1):
            result += S[j]
    print(result)
if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    solved18(N,S)