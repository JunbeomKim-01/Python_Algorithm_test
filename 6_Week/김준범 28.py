import sys

v = int(sys.stdin.readline())
node_graph = [[] for _ in range(v + 1)]
for i in range(v):
    path = list(map(int, sys.stdin.readline().split()))

    # 각 입력 Line의 정보를 받아 Parsing 후 node_graph에 연결 정보 저장
    path_len = len(path)
    for i in range(1, path_len // 2):
        node_graph[path[0]].append([path[2 * i - 1], path[2 * i]])

# 첫 번째 DFS 결과
result_first = [0 for _ in range(v + 1)]


def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            DFS(e, matrix, result)


DFS(1, node_graph, result_first)  # 아무 노드에서 시작해준다
result_first[1] = 0  # 루트 노드가 정해져 있지 않아 양방향으로 입력을 받기 때문에 해당

tmpmax = 0  # 최댓값 구하기
index = 0  # 최장경로 노드

for i in range(len(result_first)):
    if tmpmax < result_first[i]:
        tmpmax = result_first[i]
        index = i

# 최장경로 노드에서 다시 DFS를 통해 트리의 지름을 구함
result_final = [0 for _ in range(v + 1)]
DFS(index, node_graph, result_final)
result_final[index] = 0
print(max(result_final))