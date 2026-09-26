class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        rem = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            r = total % k
            if r in rem:
                if i - rem[r] >= 2:
                    return True
            else:
                rem[r] = i
        return False