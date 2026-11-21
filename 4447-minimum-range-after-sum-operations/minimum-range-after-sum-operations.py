class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        arr=[a,b,c]
        while True:
            arr.sort()
            if arr[0]+arr[1]<arr[2]:
                arr[2]=arr[0]+arr[1]
                continue
            else:
                break
        return arr[2]-arr[0]

# Do nothing:range=z−x
# Replace z with x+y:range=x there ans=min(z-x,x)



