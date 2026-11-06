#USE MAXHEAP
import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles=[-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            num=-heapq.heappop(piles)
            num-=num//2
            heapq.heappush(piles,-num)
        return -sum(piles)
# max heap me max element at top
# min heap me min element at top
# find the max number then make it num//2 then push back in heap 