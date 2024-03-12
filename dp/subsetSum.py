# Subset Sum Problem

def subsetSum(arr, n, sum):
    # print("n: ", n, "sum: ", sum)
    if sum == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > sum:
        return subsetSum(arr, n-1, sum)
    return subsetSum(arr, n-1, sum) or subsetSum(arr, n-1, sum-arr[n-1])

print(subsetSum([3, 34, 4, 12, 5, 2], 6, 9))
# complexity: O(2^n)

# Dynamic Programming
def subsetSumDp(arr, n, sum):
    dp = [[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, sum+1):
        dp[0][i] = False
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sum]

print(subsetSumDp([3, 34, 4, 12, 5, 2], 6, 9))

# complexity: O(n*sum)