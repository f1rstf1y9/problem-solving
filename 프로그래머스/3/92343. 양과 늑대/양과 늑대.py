max_sheep = 0

def solution(info, edges):
    global max_sheep
    
    node_count = len(info)
    glassland = [[] for _ in range(node_count)]
    for a, b in edges:
        glassland[a].append(b)
        glassland[b].append(a)
    
    visited = [[[False]*18 for _ in range(18)] for _ in range(node_count)]
    
    def backtracking(cur_node, cur_sheep, cur_wolf):
        global max_sheep
        
        max_sheep = max(max_sheep, cur_sheep)
        for next_node in glassland[cur_node]:
            if not visited[next_node][cur_sheep][cur_wolf]:
                next_sheep, next_wolf = cur_sheep, cur_wolf
                next_node_info = info[next_node]
                if next_node_info == 1:
                    next_wolf += 1
                elif next_node_info == 0:
                    next_sheep += 1
                if next_sheep > next_wolf:
                    info[next_node] = -1
                    visited[next_node][next_sheep][next_wolf] = 1
                    backtracking(next_node, next_sheep, next_wolf)
                    info[next_node] = next_node_info
                    visited[next_node][next_sheep][next_wolf] = 0
    
    info[0] = -1
    visited[0][1][0] = 1
    backtracking(0, 1, 0)
    
    return max_sheep