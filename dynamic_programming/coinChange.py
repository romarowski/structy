def coinChange(coins, amount):
    def dp(coins, amount):
        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')
    
        min_coins = float('inf')
        for coin in coins:
            n_coins = 1 + dp(coins, amount-coin)
            min_coins = min(min_coins, n_coins)
        
        return min_coins

    ans = dp(coins, amount)
    if ans == float('inf'):
        return -1
    return ans

print(coinChange([2, 1, 3], 4))