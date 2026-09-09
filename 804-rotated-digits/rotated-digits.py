class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            s = str(i)

            if not any(x in s for x in "347") and any(x in s for x in "2569"):
                ans += 1

        return ans