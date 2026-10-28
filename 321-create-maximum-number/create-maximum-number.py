class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def bdanum(arr,k):
           stack=[]
           remove=len(arr)-k
           for num in arr:
               while stack and remove>0 and num>stack[-1]:
                     stack.pop()
                     remove-=1
               stack.append(num)
           return stack[:k]
        def merge(a,b):
            ans=[]
            while a or b:
                if a>b:
                    ans.append(a.pop(0))
                else:
                    ans.append(b.pop(0))
            return ans
        sbsebda=[]
        for i in range(k+1):
            if i>len(nums1) or k-i>len(nums2):
                continue
            phla=bdanum(nums1,i)
            dusra=bdanum(nums2,k-i)
            curr=merge(phla,dusra)
            sbsebda=max(sbsebda,curr)
        return sbsebda
            

