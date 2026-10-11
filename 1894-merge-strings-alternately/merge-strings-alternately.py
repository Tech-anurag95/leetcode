class Solution:
    def mergeAlternately(self,word1:str,word2:str)->str:
        x=""
        i=0
        while i<len(word1) or i<len(word2): #agar word1 khatam hogya but word2 abhi bhi hai
            if i<len(word1):
                x+=word1[i]
            if i<len(word2):
                x+=word2[i]
            i+=1
        return x