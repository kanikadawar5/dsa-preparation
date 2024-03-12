# Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.

def countWays(m, n, x):
    dp = [[0 for i in range(x+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(x+1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            if i == 1 and j != 0 and j <= x:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    return dp[n-1][x-2] + dp[n-1][x-1]


# def countWays(m,n,x):
#     dp = [[0 for i in range(x+1)] for j in range(n+1)]
#     for i in range(1, m+1):
#         dp[1][i] = 1
#     for i in range(2, n+1):
#         for j in range(1, x+1):
#             for k in range(1, m+1):
#                 if j >= k:
#                     dp[i][j] += dp[i-1][j-k]
#     return dp[n][x]


# print(countWays(6, 4, 7))  # 6
print(countWays(4, 2, 5))  # 4
