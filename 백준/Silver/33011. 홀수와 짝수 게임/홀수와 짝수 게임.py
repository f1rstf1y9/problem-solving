for _ in range(int(input())):
    N = int(input())
    A = list()
    odd_cnt = sum(1 for x in map(int, input().split()) if x%2)
    even_cnt = N - odd_cnt
    
    if (odd_cnt == even_cnt) or (odd_cnt-1 >= even_cnt and odd_cnt%2 == 0) or (even_cnt-1 >= odd_cnt and even_cnt%2 == 0):
        print("heeda0528")
    else:
        print("amsminn")