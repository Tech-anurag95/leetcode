class Solution:
    def reverseWords(self,s:str)->str:
        words=s.split()
        vowels="aeiou"
        count=0
        for ch in words[0]:
            if ch in vowels: count+=1
        for i in range(1,len(words)):
            c=0
            for ch in words[i]:
                if ch in vowels: c+=1
            if c==count: words[i]=words[i][::-1]
        return " ".join(words)