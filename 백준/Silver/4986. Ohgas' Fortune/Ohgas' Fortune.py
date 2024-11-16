import math

def simple_calc(amount, rate, years, charge):
    total_interest = 0
    for _ in range(years):
        total_interest += math.floor(amount * rate)
        amount -= charge
    return amount + total_interest

def compound_calc(amount, rate, years, charge):
    for _ in range(years):
        interest = math.floor(amount * rate)
        amount += interest
        amount -= charge
    return amount
    
m = int(input())
for _ in range(m):
    amount = int(input())
    years = int(input())
    n = int(input())
    
    final_amount = 0
    for _ in range(n):
        operation = input().split()
        type = int(operation[0])
        rate = float(operation[1])
        charge = int(operation[2])
        
        if type == 0:
            cur_amount = simple_calc(amount, rate, years, charge)
        else:
            cur_amount = compound_calc(amount, rate, years, charge)
        final_amount = max(final_amount, cur_amount)
    print(final_amount)