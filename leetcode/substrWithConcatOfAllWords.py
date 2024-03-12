from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        words_count = Counter(words)
        indices = []

        for i in range(len(s) - total_len + 1):
            seen = Counter()
            for j in range(total_words):
                word = s[i + j * word_len: i + (j + 1) * word_len]
                if word not in words_count:
                    break
                seen[word] += 1
                if seen[word] > words_count[word]:
                    break
                if j + 1 == total_words:
                    indices.append(i)

        return indices

# Test cases
print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))  # [0, 9]
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # []
