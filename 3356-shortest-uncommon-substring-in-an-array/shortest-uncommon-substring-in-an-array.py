class Solution:
    def shortestSubstrings(self,arr:List[str])->List[str]:
        ans=[]

        for i,word in enumerate(arr):
            substring=set()

            for j in range(len(word)):
                for k in range(j+1,len(word)+1):
                    substring.add(word[j:k])

            shortest=""

            for sub in substring:
                found=True

                for j,other in enumerate(arr):
                    if i==j:
                        continue

                    if sub in other:
                        found=False
                        break

                if found:
                    if shortest=="" or len(sub)<len(shortest):
                        shortest=sub
                    elif len(sub)==len(shortest) and sub<shortest:
                        shortest=sub

            ans.append(shortest)

        return ans