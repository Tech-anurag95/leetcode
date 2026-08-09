class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        from collections import Counter
        count=Counter(nums)
        for key,value in count.items():
            if value==2:
                a.append(key)
        return a