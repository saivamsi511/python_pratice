prices = [7,1,5,3,6,4]
min_purchase =  prices[0]
max_profit = 0
for val in prices:
    temp = val - max_profit
    if temp >max_profit:
        max_profit=temp
    if val<min_purchase:
        min_purchase = val
print(max_profit)
