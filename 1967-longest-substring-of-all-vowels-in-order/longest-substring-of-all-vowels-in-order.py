class Solution:
    def longestBeautifulSubstring(self,word:str)->int:
        left=0
        count=1
        ans=0
        for right in range(1,len(word)):
            if word[right]<word[right-1]:
                left=right
                count=1
            elif word[right]>word[right-1]:
                count+=1
            if count==5:
                ans=max(ans,right-left+1)
        return ans