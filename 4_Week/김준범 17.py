import sys
input = sys.stdin.readline

def solved17(N):
    li = list(map(int,str(N)))
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        lesser_arr, equal_arr, greater_arr = [], [], []
        for num in arr:
            if num > pivot:
                lesser_arr.append(num)
            elif num < pivot:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
        return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
    li = quick_sort(li)

    for i in li:
        print(i, end='')

if __name__ == '__main__':
    N = int(input())
    solved17(N)