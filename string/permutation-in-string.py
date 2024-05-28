class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        track = {}
        small = s1
        big = s2
        if len(s2) < len(s1):
            return False
        for s in small:
            track[s] = track.get(s, 0) + 1
        checker = track.copy()

        s = 0
        for i in range(len(big)):
            c = big[i]
            if c in checker:
                checker[c] -= 1
                while checker[c] < 0:
                    cdel = big[s]
                    if cdel in checker:
                        checker[cdel] += 1
                    s += 1
            else:
                s = i+1
                checker = track.copy()
            if all(value == 0 for value in checker.values()):
                return True
        return False