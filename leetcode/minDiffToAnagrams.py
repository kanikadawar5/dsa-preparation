class Solution:
    def findDiff(self, s, t):
        occS = {}
        diff = 0
        for ch in s:
            if ch in occS:
                occS[ch] += 1
            else:
                occS[ch] = 1
        for ch in t:
            if ch in occS:
                occS[ch] -= 1
                if occS[ch] == 0:
                    del occS[ch]
            else:
                diff += 1
        return diff

    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        return min(self.findDiff(s, t), self.findDiff( t, s))

print(Solution().minSteps("bab", "aba")) # 1
print(Solution().minSteps("leetcode", "practice")) # 5
print(Solution().minSteps("anagram", "mangaar")) # 0