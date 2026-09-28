class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        from collections import Counter
        count=0
        total=0
        dictionary=Counter({x:0 for x in set(labels)})
        items=sorted(zip(values,labels),reverse=True)
        for value,label in items:
            if dictionary[label]<useLimit:
                total+=value
                dictionary[label]+=1
                count+=1
                if count==numWanted:
                    break
        return total