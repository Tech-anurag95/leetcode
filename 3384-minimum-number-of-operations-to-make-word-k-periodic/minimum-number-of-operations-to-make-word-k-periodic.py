from collections import Counter
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        freq=Counter()
        for i in range(0,len(word),k):
            freq[word[i:i+k]]+=1
        return len(word)//k-max(freq.values())