class Solution:
    def findScore(self,nums:List[int])->int:
        count=0
        a=[True]*len(nums)
        arr=sorted((num,i) for i,num in enumerate(nums))
        for num,i in arr:
            if a[i]:
                count+=num
                a[i]=False
                if i>0:
                    a[i-1]=False
                if i<len(nums)-1:
                    a[i+1]=False
        return count