from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        count[0]=1                          # empty prefix has remainder 0, seen once
        prefix_sum=0
        result=0
        for num in nums:
            prefix_sum+=num
            remainder=prefix_sum % k        # in Python, always in [0, k-1] for positive k
            result+=count[remainder]        # subarrays ending here that are divisible
            count[remainder]+=1
        return result