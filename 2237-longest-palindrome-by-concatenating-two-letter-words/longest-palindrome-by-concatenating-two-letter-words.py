class Solution:
    def longestPalindrome(self,words:List[str])->int:
        from collections import Counter
        freq=Counter(words)
        count=0
        center=False
        for num in freq:
            if len(set(num))==1:
                count+=(freq[num]//2)*4
                if freq[num]%2==1:
                    center=True
            elif num[::-1] in freq:
                pairs=min(freq[num],freq[num[::-1]])
                count+=pairs*4
                freq[num]=0
                freq[num[::-1]]=0
        for num in freq:
            if len(set(num))==1 and freq[num]%2==1:
                center=True
        if center:
            count+=2
        return count