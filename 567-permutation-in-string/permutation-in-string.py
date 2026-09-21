from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)

        if len(s1) > len(s2):
            return False

        for i in range(len(s2) - l + 1):
            if Counter(s2[i:i+l]) == Counter(s1):
                return True

        return False