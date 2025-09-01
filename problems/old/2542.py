import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        hp = []
        total = 0
        ans = 0

        n2 = [(v, i) for i, v in enumerate(nums2)]

        n2.sort(key=lambda a: a[0])

        for _ in range(k - 1):
            ele = n2.pop()
            total += nums1[ele[1]]
            heapq.heappush(hp, nums1[ele[1]])

        for _ in range(len(n2)):
            ele = n2.pop()
            total+= nums1[ele[1]]
            new_ans = total * ele[0]
            
            ans = new_ans if ans < new_ans else ans

            total -= heapq.heappushpop(hp, nums1[ele[1]])
            
            

        return ans


s = Solution()


# Example 1:

# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation:
# The four possible subsequence scores are:
# - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
# - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
# - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
# - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
# Therefore, we return the max score, which is 12.

print(s.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))
# Example 2:

# Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
# Output: 30
# Explanation:
# Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
print(s.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))


# 168
print(s.maxScore([2, 1, 14, 12], [11, 7, 13, 6], 3))


# 1364
print(s.maxScore([22, 5, 25, 15, 28, 1], [22, 30, 25, 25, 9, 18], 3))


# 22 30 25
# 22 5 25
