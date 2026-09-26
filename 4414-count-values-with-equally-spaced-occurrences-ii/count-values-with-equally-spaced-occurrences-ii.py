class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        index={}
        
        for i,num in enumerate(nums):
            if num not in index:
                index[num]=[]
            index[num].append(i)

        ans=0

        for indexes in index.values():
            if len(indexes)<3:
                continue

            diff=indexes[1]-indexes[0]
            valid=True

            for i in range(2,len(indexes)):
                if indexes[i]-indexes[i-1]!=diff:
                    valid=False
                    break

            if valid:
                ans+=1

        return ans