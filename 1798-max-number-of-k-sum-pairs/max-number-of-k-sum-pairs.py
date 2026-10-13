# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         count=0
#         left=0
#         right=len(nums)-1
#         while left<right:
#             if nums[left]+nums[right]==k:
#                 count+=1
#                 right-=1
#                 left+=1
#             elif nums[left]+nums[right]>k:
#                 right-=1
#             else:
#                 left+=1
#         return count

        

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0

        for num in nums:
            need = k - num

            if seen.get(need, 0) > 0:
                count += 1
                seen[need] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return count