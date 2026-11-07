class Solution:
    def countElements(self, nums: List[int]) -> int:
        chota=float("inf")
        bda=float("-inf")
        for num in nums:
            chota=min(chota,num)
            bda=max(bda,num)
        count=0
        for i in nums:
            if i>chota and i<bda:
                count+=1
        return count
