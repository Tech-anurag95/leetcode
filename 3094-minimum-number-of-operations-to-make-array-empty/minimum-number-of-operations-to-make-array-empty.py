# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         freq=Counter(nums)
#         ans=0
#         for f in freq.values():
#             if f==1:
#                 return -1
#             if f%3==0:
#                 ans+=f//3
#             elif f%3==1:
#                 ans+=(f-4)//3+2
#             else:
#                 ans+=f//3+1
#         return ans

#         '''any number>2 can be expressed in form of 3k+1 or 3k+2 
#         for freq=1 then it can never be deleted so return -1
#         if freq of form 3k+1 then ((freq-4)//3)+2
#         if freq of form 3k+2 then (freq//3)+1'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ans=0

        for f in freq.values():
            if f==1:
                return -1
            ans+=f//3
            if f%3!=0:
                ans+=1

        return ans