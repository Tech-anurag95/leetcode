class Solution:
    def mergeCharacters(self,s,k):
        i=0
        while i<len(s):
            j=i+1
            merged=False
            while j<len(s):
                if s[i]==s[j] and j-i<=k:
                    s=s[:j]+s[j+1:]
                    merged=True
                    break
                j+=1
            if merged:
                i=0
            else:
                i+=1
        return s