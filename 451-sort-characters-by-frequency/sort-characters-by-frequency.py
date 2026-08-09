class Solution:
    def frequencySort(self, s: str) -> str:
        a=""
        dict={}
        for char in s:
            if char not in a:
              a+=char
              dict[char]=s.count(char)
        sorted_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for char,freq in sorted_dict:
            ans+=char*freq
        return ans
        
