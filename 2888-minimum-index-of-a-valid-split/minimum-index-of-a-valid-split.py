class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        max_freq=0
        dominant=0
        for key,value in freq.items():
            if value>max_freq:
                max_freq=value
                dominant=key

        left=0
        for i in range(len(nums)-1):
            if nums[i]==dominant:
                left+=1

            right=max_freq-left

            if left>(i+1)//2 and right>(len(nums)-i-1)//2:
                return i
        return -1