class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        words.sort()
        ans=[]
        for top in words:
            for left in words:
                for right in words:
                    for bottom in words:
                        if len({top,left,right,bottom})<4:
                            continue
                        if top[0]==left[0] and top[3]==right[0] and bottom[0]==left[3] and bottom[3]==right[3]:
                            ans.append([top,left,right,bottom])
        return ans