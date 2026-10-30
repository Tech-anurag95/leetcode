class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev=float('-inf')
        ans=0
        for pair in pairs:
            if prev<pair[0]:
                prev=pair[1]
                ans+=1
        return ans