import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
scc = [-1] * (n + 1)
scc_num = 0
d = [0] * (n + 1)
finished = [False] * (n + 1)
node_idx = 0
st = []
scc_size = []


def dfs(x):
    global node_idx, scc_num
    node_idx += 1
    d[x] = node_idx
    st.append(x)
    parent = d[x]
    for y in graph[x]:
        if d[y] == 0:
            parent = min(parent, dfs(y))
        elif not finished[y]:
            parent = min(parent, d[y])
    if parent == d[x]:
        scc_size_num = 0
        while True:
            scc_size_num += 1
            s = st.pop()
            scc[s] = scc_num
            finished[s] = True
            if s == x:
                break
        scc_num += 1
        scc_size.append(scc_size_num)

    return parent


for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for j in range(1, n + 1):
    if d[j] == 0:
        dfs(j)

scc_graph = [set() for _ in range(scc_num)]
scc_graph_inv = [set() for _ in range(scc_num)]

for i in range(1, n + 1):
    for j in graph[i]:
        if scc[i] != scc[j]:
            scc_graph[scc[i]].add(scc[j])
            scc_graph_inv[scc[j]].add(scc[i])

scc_graph_outnum = [len(scc_graph[i]) for i in range(scc_num)]

scc_childs = [set() for _ in range(scc_num)]
q = [i for i in range(scc_num) if scc_graph_outnum[i] == 0]
while q:
    temp = []
    for i in q:
        scc_childs[i].add(i)
        for j in scc_graph_inv[i]:
            scc_childs[j] |= scc_childs[i]
            scc_graph_outnum[j] -= 1
            if scc_graph_outnum[j] == 0:
                temp.append(j)
    q = temp
node_child_num = [sum(scc_size[j] for j in scc_childs[i]) for i in range(scc_num)]
m = max(node_child_num)

for i in range(1, n + 1):
    if node_child_num[scc[i]] == m:
        print(i, end=" ")