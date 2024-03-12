# Longest Substring Without Repeating Characters
# add comments in each line of code to understand the code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        occ = {}
        for right in range(len(s)):
            if s[right] in occ:
                # if the character is already in the occurence dictionary, then update the left pointer to the next character of the occurence of the character
                left = max(left, occ[s[right]] + 1)
            # update the occurence of the character to the right pointer
            occ[s[right]] = right
            # update the maxLen to the maximum of the current maxLen and the difference between the right and left pointers
            maxLen = max(maxLen, right - left + 1)
        return maxLen


print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
