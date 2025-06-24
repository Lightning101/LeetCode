class Solution:

    def findCombo(self, idx, candidates, target, ans, used, total, candidates_size):
        if idx >= candidates_size or total > target:
            return
        elif total == target:
            ans.append(used[:])
            return

        self.findCombo(
            idx,
            candidates,
            target,
            ans,
            used[:] + [candidates[idx]],
            total + candidates[idx],
            candidates_size,
        )
        self.findCombo(
            idx + 1, candidates, target, ans, used[:], total, candidates_size
        )

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates_size = len(candidates)
        self.findCombo(0, candidates, target, ans, [], 0, candidates_size)
        return ans


s = Solution()

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

print(s.combinationSum([2, 3, 6, 7], 7))

# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
print(s.combinationSum([2, 3, 5], 8))

# Input: candidates = [2], target = 1
# Output: []

print(s.combinationSum([2], 1))
