class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digitSum=sum(map(int,str(nums[i])))
            if digitSum==i:
                return i
        return -1