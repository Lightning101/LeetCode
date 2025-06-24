class Solution:

    def isPlacementPossible(self, positions, d, m):
        numBallsPlace = 1
        posOfLastBall = positions[0]
        for i in range(len(positions)):
            if positions[i] >= posOfLastBall + d:
                numBallsPlace += 1
                posOfLastBall = positions[i]
        return not numBallsPlace < m

    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        ans = left

        while left <= right:
            mid = (left + right) // 2
            if self.isPlacementPossible(position, mid, m):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans


s = Solution()

# print(s.maxDistance([1, 2, 3, 4, 7], 3))
# print(s.maxDistance([5,4,3,2,1,1000000000],2))
print(s.maxDistance([1,2,3,4,5,6,7,8,9,10],4))
