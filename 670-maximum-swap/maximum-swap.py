class Solution:
    def maximumSwap(self, num: int) -> int:
        arr=list(map(int,str(num)))
        for i in range(len(arr)-1):
            if arr[i]<max(arr[i+1:]):
                start=i
                break
        else:
            return num         #number is already largest
        maxi=max(arr[start+1:])
        for j in range(len(arr)-1,start,-1):
            if arr[j]==maxi:
                arr[start],arr[j]=arr[j],arr[start]
                break
        return int(''.join(map(str,arr)))