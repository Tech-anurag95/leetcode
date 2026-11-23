class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col=n-1
        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False

# if we start from matrix[0][0] then both up and down is increasing so we wont be able to apply binary search thats why we start from top right cause in the left of top right we have decreasing and down of top right is increasing so we can apply binary search easily

