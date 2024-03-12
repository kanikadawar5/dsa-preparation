# the problem does

def coinChange(sum, coins):
    dp = [0 for i in range(sum+1)]
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], sum+1):
            dp[j] += dp[j - coins[i]]
    return dp[sum]


print(coinChange(5, [1, 2, 5]))
print(coinChange(4, [1, 2, 3]))
print(coinChange(3, [2]))
