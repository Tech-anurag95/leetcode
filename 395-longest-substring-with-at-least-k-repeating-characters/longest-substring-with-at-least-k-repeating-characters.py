class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if len(s) < k:         #agar k ki value len se bhi bdi hogyi to koi possible nhi hai 
            return 0

        for ch in set(s):

            count = s.count(ch)

            if count < k:

                parts = s.split(ch)  # ye wo element dhundhega jo k se kam baar appear hua hai string me (splitting point)

                ans = 0

                for part in parts:
                    length = self.longestSubstring(part, k) 
                    ans = max(ans, length)

                return ans

        return len(s)