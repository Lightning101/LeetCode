# class Solution:
#     def hIndex(self, citations: list[int]) -> int:

#         citations.sort()

#         ans = 0
#         for i in range(len(citations) - 1, -1, -1):
#             if citations[i] > ans:
#                 ans += 1
#             else:
#                 break
#         return ans


#     public class Solution {
#     public int hIndex(int[] citations) {
#         int n = citations.length;
#         int[] papers = new int[n + 1];
#         // counting papers for each citation number
#         for (int c: citations)
#             papers[Math.min(n, c)]++;
#         // finding the h-index
#         int k = n;
#         for (int s = papers[n]; k > s; s += papers[k])
#             k--;
#         return k;
#     }
# }


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        size = len(citations)
        papers = [0] * (size + 1)

        for i in citations:
            papers[min(i, size)] += 1

        ans = size
        s = papers[size]
        while ans > s:
            ans -= 1
            s += papers[ans]

        return ans


s = Solution()


# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
print(s.hIndex([3, 0, 6, 1, 5]))

# Example 2:

# Input: citations = [1,3,1]
# Output: 1
print(s.hIndex([1, 3, 1]))


# 1
print(s.hIndex([0, 0, 2]))

# 1
print(s.hIndex([1, 1]))

# 2
print(s.hIndex([11, 15]))


print(s.hIndex([1, 3, 2, 3, 5]))
