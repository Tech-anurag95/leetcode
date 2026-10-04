class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        dic = {}
        currlen = 0
        for right in range(len(nums)):
            dic[nums[right]] = dic.get(nums[right], 0) + 1
            while dic[nums[right]] > k:
                dic[nums[left]] -= 1
                left += 1
            currlen = max(currlen, right - left + 1)
        return currlen