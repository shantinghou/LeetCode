class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        longest = 0
        acc = 0
        c = 0
        while c < len(s):
            car = s[c]
            if car in seen and len(seen[car]) > 0:
                bC = seen[car][0]
                if bC >= acc:
                    acc = bC + 1
            seen[car] = [c]
            c += 1
            if c - acc > longest:
                longest = c - acc
        if c - acc > longest:
            longest = c - acc
        return longest

        
        























        # seen = {}
        # longest = 0
        # b = 0
        # for i in range (len(s)):
        #     a = s[i]
        #     if a in seen and seen[a] >= b:
        #         b = seen[a] + 1
        #     else:
        #         longest = max(longest, i-b+1)
        #     seen[a] = i
        # return longest
            