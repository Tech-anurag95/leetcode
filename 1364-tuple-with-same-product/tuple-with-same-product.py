# soltuin se hint dekh ke kiya hu
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums):
        product_count=defaultdict(int)
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                ans+=8*product_count[product]  #kisi bhi do pairs ka 4 element ka tuple bnane ka 8 ways hota hai 
                # example for pair (2,6) and (3,4)
                # (2,6,3,4)
                # (6,2,3,4)
                # (2,6,4,3)
                # (6,2,4,3)
                # (3,4,2,6)       
                # (4,3,2,6)
                # (3,4,6,2)
                # (4,3,6,2)
                product_count[product]+=1
        return ans
