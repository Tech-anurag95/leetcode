class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result=[]

        for i in range(len(nums)-k+1):
            power=nums[i]

            for j in range(i+1,i+k):
                if nums[j]!=nums[j-1]+1:
                    power=-1
                    break
                power=nums[j]

            result.append(power)

        return result