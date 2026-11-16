class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        dic={}  #isme word2 ke har alphabet ki max freq
        for word in words2:
            curr={}
            for ch in word:
                curr[ch]=curr.get(ch,0)+1
            for ch in curr:
                dic[ch]=max(dic.get(ch,0),curr[ch])
        ans=[]
        for word in words1:
            curr={}
            for ch in word:
                curr[ch]=curr.get(ch,0)+1
            flag=True
            for ch in dic:
                if dic.get(ch,0)>curr.get(ch,0):
                    flag=False
                    break
            if flag:
                ans.append(word)
        return ans 


            



