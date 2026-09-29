class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        a=[]
        b=[]
        if len(word1)!=len(word2):
            return False
        if set(word1) != set(word2):
            return False
        dic1=Counter(word1)
        dic2=Counter(word2)
        for phla in dic1.values():
            a.append(phla)
        for dusra in dic2.values():
            b.append(dusra)
        a.sort()
        b.sort()
        return a==b
        
        
        
        
            