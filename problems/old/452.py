# class Solution:
#     def findMinArrowShots(self, points: list[list[int]]) -> int:
#         points.sort()
#         ans = 0
#         k = points[0][1]
#         for i in range(1, len(points)):
#             [start, end] = points[i]
#             if k < start:
#                 ans += 1
#                 k = end
#             else:
#                 k = k if k < end else end
#         return ans + 1


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        k = points[0][1]

        ans = 1
        for i in range(len(points)):
            if k < points[i][0]:
                ans += 1
                k = points[i][1]

        return ans


s = Solution()


# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
print(s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))

# 2
print(s.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
