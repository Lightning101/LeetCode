class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            if curr > ans:
                ans = curr

        return ans


s = Solution()
# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# print(s.largestAltitude([-5, 1, 5, 0, -7]))
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
print(s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
