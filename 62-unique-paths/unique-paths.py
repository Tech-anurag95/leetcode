class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m): #first row elemt =1
            dp[i][0]=1
        for j in range(n): # first column element =1
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]



        #  dp = [[1]*n for _ in range(m)]
        #  for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]

        # we can skill filling first row and column element 1 if we initialize matrix with 1 as its elements instead of 0