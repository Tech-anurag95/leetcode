class Solution:
    def maxSatisfied(self,customers:list[int],grumpy:list[int],minutes:int)->int:
        alreadysatisfied=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                alreadysatisfied+=customers[i]

        window=0
        ans=0
        left=0

        for right in range(len(customers)):
            if grumpy[right]==1:
                window+=customers[right]

            if right-left+1>minutes:
                if grumpy[left]==1:
                    window-=customers[left]
                left+=1

            ans=max(ans,window)

        return alreadysatisfied+ans