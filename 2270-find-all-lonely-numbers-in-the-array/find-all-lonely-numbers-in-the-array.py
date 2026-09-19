class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        freq={}
        for x in nums:
            freq[x] = freq.get(x, 0)+1
        a=[]
        for x in nums:
            if freq[x] == 1 and x-1 not in freq and x+1 not in freq:
                a.append(x)
        return a