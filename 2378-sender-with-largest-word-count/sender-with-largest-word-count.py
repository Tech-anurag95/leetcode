class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        diff=float("-inf")
        dic={}
        a=[]
        for message in messages:
            a.append(message.count(" ")+1)
        for i in range(len(a)):
           if senders[i] in dic:
             dic[senders[i]]+=a[i]
           else:
             dic[senders[i]]=a[i]
        return max(dic,key=lambda x:(dic[x],x))

        