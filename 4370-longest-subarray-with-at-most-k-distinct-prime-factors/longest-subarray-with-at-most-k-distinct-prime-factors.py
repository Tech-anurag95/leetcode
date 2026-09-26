class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def factors(n):
            ans = set()
            i = 2

            while i * i <= n:
                if n % i == 0:
                    ans.add(i)
                    while n % i == 0:
                        n //= i
                i += 1

            if n > 1:
                ans.add(n)

            return ans

        pf = [factors(num) for num in nums]

        freq = {}
        distinct = 0
        left = 0
        ans = 0

        for right in range(len(nums)):
            for p in pf[right]:
                if p not in freq:
                    freq[p] = 0
                    distinct += 1
                freq[p] += 1

            while distinct > k:
                for p in pf[left]:
                    freq[p] -= 1

                    if freq[p] == 0:
                        del freq[p]
                        distinct -= 1

                left += 1

            ans = max(ans, right - left + 1)

        return ans