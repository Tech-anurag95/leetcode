class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        prefix = {0: 1}

        for i in range(len(nums)):
            sum += nums[i]

            if sum - k in prefix:
                count += prefix[sum - k]

            prefix[sum] = prefix.get(sum, 0) + 1

        return count