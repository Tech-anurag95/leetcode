class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        from math import prod
        zero=nums.count(0)
        poora=prod(x for x in nums if x!=0)
        a=[]
        if zero>1:
            return [0]*len(nums)
        for num in nums:
            if zero==1:
                if num==0:
                    a.append(poora)
                else:
                    a.append(0)
            else:
                a.append(poora//num)
        return a