def solve15(N):
    arr = []
    for _ in range(N):
        A = int(input())
        arr.append(A)

    def sort(_arr):
        if len(_arr) <= 1:
            return _arr
        pivot = _arr[len(_arr) // 2]
        lesser_arr, equal_arr, greater_arr = [], [], []
        for num in _arr:
            if num < pivot:
                lesser_arr.append(num)
            elif num > pivot:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
        return sort(lesser_arr) + equal_arr + sort(greater_arr)
    arr = sort(arr)
    for i in arr:
        print(i)
if __name__ == '__main__':
    N= int(input())
    solve15(N)