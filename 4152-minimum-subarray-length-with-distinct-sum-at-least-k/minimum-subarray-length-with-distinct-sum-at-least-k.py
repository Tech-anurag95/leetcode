class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        total=0
        dic={}
        chota=float("inf")
        while right<len(nums):
            dic[nums[right]]=dic.get(nums[right],0)+1
            if dic[nums[right]]==1:
                total+=nums[right]
            if total<k:
                right+=1
            while total>=k:
                 chota=min(chota,right-left+1)
                 dic[nums[left]]-=1
                 if dic[nums[left]]==0:
                    total-=nums[left]
                 left+=1
                 if total<k:
                     right+=1
        return chota if chota!=float("inf") else -1

     


        