import heapq
class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            num=heapq.heappop(nums)
            heapq.heappush(nums,num+1)
        ans=1
        for num in nums:
            ans=(ans*num)%(10**9+7)
        return ans