import sys

def solved20(N):
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    def merge_sort(group):
        n = len(group)
        if n <= 1:
            return
        # 그룹을 반으로 나눈다
        mid = n // 2
        group1 = group[:mid]
        group2 = group[mid:]
        # 재귀적으로 병합 정렬을 수행한다
        merge_sort(group1)
        merge_sort(group2)

        # 정렬한다
        idx, idx1, idx2 = 0, 0, 0  # 그룹전체 인덱스, 그룹1 인덱스, 그룹2 인덱스
        while idx1 < len(group1) and idx2 < len(group2):
            if group1[idx1] < group2[idx2]:
                group[idx] = group1[idx1]
                idx1 += 1
            else:
                group[idx] = group2[idx2]
                idx2 += 1
            idx += 1

        # 그룹에 남아있는 원소를 넣는다
        while idx1 < len(group1):
            group[idx] = group1[idx1]
            idx1 += 1
            idx += 1
        while idx2 < len(group2):
            group[idx] = group2[idx2]
            idx2 += 1
            idx += 1
    merge_sort(numbers)

    for num in numbers:
        print(num)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    solved20(N)