class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ans=[]
        lastindex={}
        # Store last occurrence of every character
        for i in range(len(s)):
            lastindex[s[i]]=i
        currmax=0
        start=0
        for i in range(len(s)):
            currmax=max(currmax,lastindex[s[i]])
            if i==currmax:
                ans.append(i-start+1)
                start=i+1
        return ans


# lastindex[s[i]] → Last occurrence of the current character.
# currmax → Farthest last occurrence among all characters in the current partition.
# i == currmax → Current partition can safely end here