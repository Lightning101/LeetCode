# class Solution:
#     def numberofWays(self, target, idx, nums,size, memo):
#         if (target, idx) in memo:
#             return memo[(target, idx)]
#         if idx == size:
#             if( target == 0 and  nums[idx] == 0):
#                 return 2
#             elif target + nums[idx] == 0 or target - nums[idx] == 0:
#                 return 1
#             else:
#                 return 0
#         memo[(target, idx)] = self.numberofWays(
#             target + nums[idx], idx + 1, nums,size, memo
#         ) + self.numberofWays(target - nums[idx], idx + 1, nums,size, memo)
#         return memo[(target, idx)]

#     def findTargetSumWays(self, nums: list[int], target: int) -> int:
#         return self.numberofWays(target, 0, nums,len(nums) -1, {})


from functools import cache
from cProfile import Profile
from pstats import SortKey, Stats


class Solution:

    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        size = len(nums)

        @cache
        def numberofWays(
            target,
            idx,
        ):
            if idx == size - 1:
                if target == 0 and nums[idx] == 0:
                    return 2
                elif target + nums[idx] == 0 or target - nums[idx] == 0:
                    return 1
                else:
                    return 0
            return numberofWays(target + nums[idx], idx + 1) + numberofWays(
                target - nums[idx], idx + 1
            )
        ans = 0
        with Profile() as profile:
            ans = numberofWays(target, 0)
            (Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats())
        return ans


s = Solution()

print(s.findTargetSumWays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3))
# print(s.findTargetSumWays([1, 0], 1))
# print(s.findTargetSumWays([1],1))
