from collections import Counter

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        d = Counter(nums)
        a = []
        for x in nums:
            if d[x] == 1 and x-1 not in d and x+1 not in d:
                a.append(x)

        return a