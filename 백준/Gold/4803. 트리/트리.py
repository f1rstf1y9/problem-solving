import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]
    
def union(a, b, parents):
    a = find(a, parents)
    b = find(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def count_trees(n, m):
    parents = [i for i in range(n+1)]
    cycle = set()
    
    for _ in range(m):
        e1, e2 = map(int, input().split())
        if find(e1, parents) == find(e2, parents):
            cycle.add(parents[e1])
            cycle.add(parents[e2])
        elif parents[e1] in cycle or parents[e2] in cycle:
            cycle.add(parents[e1])
            cycle.add(parents[e2])
        union(e1, e2, parents)
    
    for i in range(n+1):
        find(i, parents)

    trees_cnt = 0
    for i in range(1, n+1):
        if parents[i] == i and i not in cycle:
            trees_cnt += 1
    
    return trees_cnt

tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    trees_cnt = count_trees(n, m)

    if trees_cnt == 0:
        print(f"Case {tc}: No trees.")
    elif trees_cnt == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {trees_cnt} trees.")
    
    tc += 1