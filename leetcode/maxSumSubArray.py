class Solution:
    def maxSumSubArray(self, N, arr, K):
        left = 0
        maxSum = 0
        currSum = 0

        for right in range(N):
            currSum += arr[right]
            if right >= K - 1:
                maxSum = max(maxSum, currSum)
                currSum -= arr[left]
                left += 1
        return maxSum


sol = Solution()
print(sol.maxSumSubArray(5, [1, 2, 3, 4, 5], 3))  # 12
print(sol.maxSumSubArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # 27
