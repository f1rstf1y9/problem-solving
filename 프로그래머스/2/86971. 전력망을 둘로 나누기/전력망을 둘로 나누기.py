'''
송전탑 개수 n : 2 ~ 100
전선 연결 정보 wires : 길이가 n-1인 정수형 2차원 배열
  - wires 원소 [v1,v2] : v1, v2가 연결되어 있음
  
전선 중 하나를 끊어서 송전탑 개수를 최대한 비슷하게 맞췄을 때, 송전탐 개수 차이
'''
from collections import deque

def solution(n, wires):
    answer = n
    
    tree = [[] for _ in range(n)]
    for v1, v2 in wires:
        tree[v1-1].append(v2-1)
        tree[v2-1].append(v1-1)
        
    def bfs(start_node, invalid_node):
        visited = [False]*n
        visited[start_node] = True
        q = deque([start_node])
        count = 1
        while q:
            node = q.popleft()
            for next_node in tree[node]:
                if next_node != invalid_node and not visited[next_node]:
                    visited[next_node] = True
                    count += 1
                    q.append(next_node)
        return count
    
    for v1, v2 in wires:
        v1_count = bfs(v1-1, v2-1)
        v2_count = bfs(v2-1, v1-1)
        
        answer = min(answer, abs(v1_count - v2_count))    
    
    return answer