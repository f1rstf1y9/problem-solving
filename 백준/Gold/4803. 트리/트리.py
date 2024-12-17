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
    is_tree = [True]*(n+1)
    
    for _ in range(m):
      v1, v2 = map(int, input().split())
      r1 = find(v1, parents)
      r2 = find(v2, parents)
      if r1 == r2:
          is_tree[r1] = False
      else:
          if not is_tree[r1] or not is_tree[r2]:
              is_tree[r1] = is_tree[r2] = False
          union(v1, v2, parents)
    
    trees_cnt = 0
    for i in range(1, n+1):
        if parents[i] == i and is_tree[i]:
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