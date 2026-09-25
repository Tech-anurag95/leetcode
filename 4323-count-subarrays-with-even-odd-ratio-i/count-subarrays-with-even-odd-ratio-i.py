class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        prefix=0
        ans=0
        count={0:1}

        for num in nums:
            if num%2==0:
                prefix+=b
            else:
                prefix-=a

            for x in count:
                if x>=prefix:
                    ans+=count[x]

            count[prefix]=count.get(prefix,0)+1

        return ans