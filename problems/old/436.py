import bisect


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        size = len(intervals)

        if size == 1:
            return [-1] if (intervals[0][0] != intervals[0][1]) else [0]

        for i in range(size):
            intervals[i].append(i)
        intervals.sort()

        ans = [-1] * size
        for i in range(1, size):
            if (
                index := bisect.bisect_left(
                    intervals, intervals[i - 1][1], key=lambda a: a[0]
                )
            ) < size:
                ans[intervals[i - 1][2]] = intervals[index][2]

        return ans


s = Solution()


# Example 1:

# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
print(s.findRightInterval([[1, 2]]))
# Example 2:

# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))
# Example 3:

# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))

# [-1,0,1]
print(s.findRightInterval([[4, 5], [2, 3], [1, 2]]))


# [3,3,3,4,5,-1]
print(s.findRightInterval([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]))
