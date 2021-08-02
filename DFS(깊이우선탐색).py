# DFS 메소드 정의

def dfs(graph, v, visited):
  # 현재노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  # 현재노드와 연결된 다른 노드를 재귀적으로 방문한다.
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문했는지 여부를 나타내기위해 리스트로 표현 (False로 초기화)
visited = [False] * 9

# 정의한 dfs함수 호출
dfs(graph,1,visited)