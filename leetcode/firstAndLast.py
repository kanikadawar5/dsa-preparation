from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                output[1] = i
                if output[0] == -1:
                    output[0] = i
        return output


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))
print(sol.searchRange([1,2,2], 2))
