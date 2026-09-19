class Solution:
    def combinationSum(self,candidates,target):
        ans=[]
        stack=[(0,[])]
        while stack:
            start,path=stack.pop()
            total=sum(path)
            if total==target:
                ans.append(path)
                continue
            if total>target:
                continue
            for i in range(start,len(candidates)):
                stack.append((i,path+[candidates[i]]))
        return ans