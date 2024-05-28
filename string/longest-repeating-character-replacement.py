class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        start = 0
        longest = 0
        for i in range(len(s)):
            c = s[i]
            seen[c] = seen.get(c, 0) + 1
            length = i + 1 - start
            if length - max(seen.values()) > k:
                cdel = s[start]
                seen[cdel] -= 1
                start += 1
            else:
                longest = max(longest, length)
        return longest
                
                