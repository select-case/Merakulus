def profit(prices):
        min_price = 100000
        profit = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            profit = max(profit,prices[i] - min_price)
        return profit


print(profit([7,1,5,3,6,4]))
print(profit([7,6,4,3,1]))