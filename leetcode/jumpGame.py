from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = [False]*(len(nums))
        for i in range(0, len(nums)):
            j = 0
            while j < nums[i] and i+j < len(nums):
                temp[i+j] = True
                j += 1
        return temp[len(temp)-1]


sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
print(sol.canJump([3, 2, 1, 0, 4]))
