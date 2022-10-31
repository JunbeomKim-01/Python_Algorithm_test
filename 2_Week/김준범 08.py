import sys
sys.setrecursionlimit(10**9)
def solve08(N,A):
    result = 0
    def quick_sort(array):
        if len(array) <= 1: return array
        pivot, tail = array[0], array[1:]
        leftSide = [x for x in tail if x <= pivot]
        rightSide = [x for x in tail if x > pivot]
        return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)
    6
    sorted_array = quick_sort(A)
    for i in range(N):
        target = sorted_array[i]
        start_index = 0
        list = sorted_array[:i] + sorted_array[i + 1:]
        end_index = len(list) - 1
        while start_index < end_index:
            _sum = list[start_index] + list[end_index]
            if target == _sum:
                result += 1
                break
            elif _sum < target:
                start_index += 1
            else:
                end_index -= 1
    print(result)


data ="10\n1 2 3 4 5 6 7 8 9 10"
N = int(data.split("\n")[0])
A = list(map(int,data.split("\n")[1].split()))


solve08(N,A)


#백준 test용

#
# import sys
# sys.setrecursionlimit(10**9)
# def p_8(N,A):
#     result = 0
#     def quick_sort(array):
#         if len(array) <= 1: return array
#         pivot, tail = int(array[0]), array[1:]
#         leftSide = [int(x) for x in tail if int(x) <= pivot]
#         rightSide = [int(x) for x in tail if int(x) > pivot]
#         return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)
#
#     sorted_array = quick_sort(A)
#     for i in range(int(N)):
#         target = sorted_array[i]
#         start_index = 0
#         list = sorted_array[:i] + sorted_array[i + 1:]
#         end_index = len(list) - 1
#
#         while start_index < end_index:
#             _sum = list[start_index] + list[end_index]
#             if target == _sum:
#                 result += 1
#                 break
#             elif _sum < target:
#                 start_index += 1
#             else:
#                 end_index -= 1
#     print(result)
#
# if __name__ == '__main__':
#     N = input()
#     A = list(map(str,input().split()))
#     p_8(N,A)