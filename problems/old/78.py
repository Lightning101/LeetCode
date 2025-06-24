class Solution:

    def combo(self, idx, combo, nums, size, ans):
        if idx == size:
            ans.append(combo)
            return

        self.combo(idx + 1, combo[:] + [nums[idx]], nums, size, ans)
        self.combo(idx + 1, combo, nums, size, ans)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.combo(0, [], nums, len(nums), ans)
        return ans


s = Solution()

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

print(s.subsets([1, 2, 3]))

# Input: nums = [0]
# Output: [[],[0]]


print(s.subsets([0]))
