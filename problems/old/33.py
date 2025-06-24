class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]

            if val >= nums[0] and target < nums[0]:
                left = mid + 1
            elif val < nums[0] and target >= nums[0]:
                right = mid -1
            else:
                if val < target:
                    left = mid + 1
                elif val > target:
                    right = mid - 1
                else:
                    ans = mid
                    break
        return ans


s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0

# nums = [4,5,6,7,0,1,2]
# target = 3

# nums = [1]
# target = 1
# nums = [1, 3]
# target = 3

print(s.search(nums, target))
