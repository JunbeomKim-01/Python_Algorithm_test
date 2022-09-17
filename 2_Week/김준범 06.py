# 이중 for문 -> 메모리 초과 -> O(n) 알고리즘으로 문제를 해결해야함 -> 투포인터 알고리즘
import sys
input = sys.stdin.readline
def solve06(N):
    array = [x for x in range(N + 1)]
    strat_index = 1
    end_index = 1
    result = 1
    _sum = 1
    # 투포인터 이동
    # sum > N -> start index ++, sum - array[start_index]
    # sum < N -> end index ++ , sum + array[end_index]
    # sum == N -> count ++, end index ++ , sum + array[end_index]
    while end_index != N:
        if _sum == N:
            result += 1
            end_index += 1
            _sum += array[end_index]
        elif _sum > N:
            _sum -= array[strat_index]
            strat_index += 1
        else:
            end_index += 1
            _sum += array[end_index]
    print(result)



data ="15"
N = int(data)


solve06(N)







