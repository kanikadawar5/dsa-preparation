# Problem - An arithmetic sequence is a list of numbers with a definite pattern. If you take any number in the sequence then subtract it from the previous one, the difference is always a constant.

# A good arithmetic sequence is an arithmetic sequence with a common difference of either 1 or -1.

# For example, [4, 5, 6] is a good arithmetic sequence. So is [6, 5, 4], [10, 9], or [-3, -2, -1]. But, [1, 2, 1] (no common difference) or [3, 7] (common difference is 4) is NOT.
# Implied, any sequence that has only one element is a good arithmetic sequence.

# For example, [4] is a good arithmetic sequence.
# Given an integer array nums, return the sum of the sums of each subarray that is a good arithmetic sequence.

# Example:

# Given nums = [7, 4, 5, 6, 5]. Each of the following subarrays is a good arithmetic sequence:

# [7], [4], [5], [6], [5],
# [4, 5], [5, 6], [6, 5],
# [4, 5, 6]
# The sums of these subarrays are:

# 7, 4, 5, 6, 5,
# 4 + 5 = 9, 5 + 6 = 11, 6 + 5 = 11,
# 4 + 5 + 6 = 15
# Thus, the answer is the sum of all the sums above, which is:

# 7 + 4 + 5 + 6 + 5 + 9 + 11 + 11 + 15 = 73.

# [5 6 7 8 9]
# [6 7 8]
def isGoodArithmetic(seq):
    if len(seq) == 1:
        return True
    diff = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False
    return True


def generateSum(nums):
    sum = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if isGoodArithmetic[i:j+1]:
                sum += sum(isGoodArithmetic[i:j+1])
    return sum
