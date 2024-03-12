from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = [word]
            else:
                anagrams[sortedWord].append(word)
        return list(anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]))
