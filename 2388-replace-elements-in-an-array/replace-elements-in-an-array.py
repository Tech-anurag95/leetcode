class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for num in operations:
            old=num[0]
            new=num[1]
            i=d[old]
            nums[i]=new
            d[new]=i
            del d[old]
        return nums