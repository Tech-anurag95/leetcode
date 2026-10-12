class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(start,subset):
            if sum(subset)==target:
                ans.append(subset.copy())
                return
            if sum(subset)>target:
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return ans

''' line 6-7-8 agar subset ka sum target ke barabar hua to answer me dal do 
        line 9-10 agar subset ka sum target se bda hua to bahar aao 
        line 11-12-13-14 ans me unique subset jayein mtlb [1,2,1] is same as [2,1,1]
        line 15-16 backtrack kro aur last element ko pop kr do '''
