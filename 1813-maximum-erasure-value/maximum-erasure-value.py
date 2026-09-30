class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = 0
        right = 0
        count = 0
        ans = 0
        a = set()

        while right < len(nums):

            if nums[right] not in a:
                a.add(nums[right])
                count += nums[right]
                right += 1
                ans = max(ans, count)

            else:
                a.remove(nums[left])
                count -= nums[left]
                left += 1

        return ans