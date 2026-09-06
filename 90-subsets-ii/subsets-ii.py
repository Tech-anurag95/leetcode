class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[[]]
        for num in nums:
            curr=[]
            for subset in out:
                curr.append(subset + [num])
            out += curr
        ans = []
        for x in out:
            if x not in ans:
                ans.append(x)
        return ans