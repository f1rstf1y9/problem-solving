a, b = map(int, input().split())
EW_dist = abs((a-1)//4 - (b-1)//4)
SN_dist = abs((a-1)%4 - (b-1)%4)
print(EW_dist + SN_dist)