cash = int(input())
stocks = list(map(int, input().split()))

init_count = cash // stocks[0]
init_cash = cash - stocks[0]*init_count

junhyun = [init_count, init_cash]
sungmin = [0, cash]

prev_stock = stocks[0]
increase_day = decrease_day = 0

for stock in stocks[1:]:
    if junhyun[1] >= stock:
        count = junhyun[1] // stock
        junhyun[0] += count
        junhyun[1] -= stock*count
    
    if prev_stock < stock:
        increase_day += 1
        decrease_day = 0
    elif prev_stock > stock:
        increase_day = 0
        decrease_day += 1
    else:
        increase_day = decrease_day = 0
    prev_stock = stock
    
    if increase_day >= 3:
        sungmin[1] += sungmin[0]*stock
        sungmin[0] = 0
    if decrease_day >= 3 and sungmin[1] >= stock:
        count = sungmin[1] // stock
        sungmin[0] += count
        sungmin[1] -= stock*count

junhyun_final = junhyun[0]*stocks[-1]+junhyun[1]
sungmin_final = sungmin[0]*stocks[-1]+sungmin[1]

if junhyun_final > sungmin_final:
    print("BNP")
elif junhyun_final < sungmin_final:
    print("TIMING")
else:
    print("SAMESAME")

    
