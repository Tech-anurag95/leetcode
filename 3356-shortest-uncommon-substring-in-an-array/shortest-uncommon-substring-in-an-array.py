class Solution:
    def shortestSubstrings(self,arr:List[str])->List[str]:
        ans=[]
        for i in range(len(arr)):
            word=arr[i]
            substrings=set()
            for j in range(len(word)):
                for k in range(j+1,len(word)+1):
                    substrings.add(word[j:k])
            shortest=""
            for eachsubstring in substrings:
                found=True
                for j in range(len(arr)):
                    if i==j:
                        continue
                    if eachsubstring in arr[j]:
                        found=False
                        break
                if found:
                    if shortest=="" or len(eachsubstring)<len(shortest):
                        shortest=eachsubstring
                    elif len(eachsubstring)==len(shortest) and eachsubstring<shortest:
                        shortest=eachsubstring
            ans.append(shortest)
        return ans