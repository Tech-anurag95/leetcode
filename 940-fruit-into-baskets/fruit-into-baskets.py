#ye tle de rha haiiiiiiiiiiiiiiiiiii
# class Solution:
#     def totalFruit(self, fruits: list[int]) -> int:
#         if len(set(fruits))==2 or len(set(fruits))==1:
#             return len(fruits)
#         left=0
#         bda=0
#         right=0
#         while right<len(fruits):
#             if len(set(fruits[left:right+1]))==1 or len(set(fruits[left:right+1]))==2:
#                 right+=1
#                 bda=max(bda,right-left)
#             else:
#                 left+=1
#         return bda

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        bda=0
        freq={}

        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1

            while len(freq)>2:
                freq[fruits[left]]-=1

                if freq[fruits[left]]==0:
                    del freq[fruits[left]]

                left+=1

            bda=max(bda,right-left+1)

        return bda

        