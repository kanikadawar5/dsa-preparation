def knapsackDp(profits, weights, capacity, n):
    dp = [[0 for i in range(capacity+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, capacity+1):
        dp[0][i] = 0
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + profits[i-1])
    return dp[n][capacity]

print(knapsackDp([60, 100, 120], [10, 20, 30], 50, 3))  
print(knapsackDp([1,2,3], [4,5,1], 5, 3))
# complexity: O(n*capacity)
# time complexity: O(n*capacity)
#  space complexity: O(n*capacity)