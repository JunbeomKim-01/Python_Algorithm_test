def solve07(N,M,array):
    start_index = 0
    end_index = N-1
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

    array_sroted = quick_sort(array)
    while start_index < end_index:
        if array_sroted[start_index] + array_sroted[end_index] == M:
            result += 1
            start_index +=1
            end_index -= 1
        elif array_sroted[start_index] + array_sroted[end_index] < M:
            start_index +=1
        else:
            end_index -= 1
    print(result)


data ="6\n9\n2 7 4 1 5 3"
N = int(data.split('\n')[0])
M = int(data.split('\n')[1])
array = list(map(int,data.split('\n')[2].split()))


solve07(N,M,array)


#백준 test 용
# def p_7(N,M,array):
#     start_index = 0
#     end_index = int(N)-1
#     result = 0
#
#     def quick_sort(arr):
#         if len(arr) <= 1:
#             return arr
#         pivot = int(arr[len(arr) // 2])
#         lesser_arr, equal_arr, greater_arr = [], [], []
#         for num in arr:
#             if int(num) < pivot:
#                 lesser_arr.append(int(num))
#             elif int(num) > pivot:
#                 greater_arr.append(int(num))
#             else:
#                 equal_arr.append(int(num))
#         return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
#
#     # def quick_sort(array):
#     #
#     #     if len(array) <= 1: return array
#     #     pivot, tail = int(array[0]), array[1:]
#     #     leftSide = [int(x) for x in tail if int(x) <= pivot]
#     #     rightSide = [int(x) for x in tail if int(x) > pivot]
#     #     return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)
#
#     array_sroted = quick_sort(array)
#
#     while start_index < end_index:
#         if array_sroted[start_index] + array_sroted[end_index] == int(M) :
#             result += 1
#             start_index +=1
#             end_index -= 1
#         elif array_sroted[start_index] + array_sroted[end_index] < int(M) :
#             start_index +=1
#         else:
#             end_index -= 1
#     print(result)
#
# if __name__ == '__main__':
#     N = input()
#     M = input()
#     array = list(map(str,input().split()))
#     p_7(N,M,array)