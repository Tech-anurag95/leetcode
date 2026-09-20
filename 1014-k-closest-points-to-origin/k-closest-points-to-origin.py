class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for point in points:
            x=point[0]
            y=point[1]
            distance=x*x+y*y
            distances.append([distance, point])
        distances.sort()
        ans = []
        for i in range(k):
            ans.append(distances[i][1])
        return ans