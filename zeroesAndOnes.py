# arr = [0,1,0,1,0,1,1,1,1]

# zeroes = 3
# 0,1,1,0

from typing import List


def sortZeroesAndOnes(nums: List) -> List:
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
    return nums

print(sortZeroesAndOnes([0,1,0,1,0,1,1,1,1]))
print(sortZeroesAndOnes([0,1,1,0]))