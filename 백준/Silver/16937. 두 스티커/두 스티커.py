H, W = map(int, input().split())
N = int(input())

stickers = [tuple(map(int, input().split())) for _ in range(N)]

max_area = 0

for i in range(N):
    for j in range(1, N):
        if i == j:
            continue
        
        w1, h1 = stickers[i]
        w2, h2 = stickers[j]
        current_area = w1 * h1 + w2 * h2
        
        if max_area >= current_area:
            continue
        
        # 1. 스티커를 모두 회전시키지 않은 상태
        if (h1 + h2 <= H and max(w1, w2) <= W) or (w1 + w2 <= W and max(h1, h2) <= H):
            max_area = current_area
            continue
        
        # 2. 1번 스티커만 회전시킨 상태
        if (w1 + h2 <= H and max(h1, w2) <= W) or (h1 + w2 <= W and max(w1, h2) <= H):
            max_area = current_area
            continue
            
        # 3. 2번 스티커만 회전시킨 상태
        if (h1 + w2 <= H and max(w1, h2) <= W) or (w1 + h2 <= W and max(h1, w2) <= H):
            max_area = current_area
            continue
            
        # 4. 두 스티커 모두 회전시킨 상태
        if (w1 + w2 <= H and max(h1, h2) <= W) or (h1 + h2 <= W and max(w1, w2) <= H):
            max_area = current_area
            continue

print(max_area)   