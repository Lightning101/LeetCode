# class Solution:
    # def countBits(self, n: int) -> list[int]:
    #     ans = [0]
    #     for i in range(1, n + 1):
    #         t = i
    #         bits = 0
    #         while i:
    #             if i % 2 == 1:
    #                 bits += 1
    #             i = i >> 1

    #         print(f"Number of Bits in {t} is {bits}")
    #         ans.append(bits)
    #     return ans
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


s = Solution()

# Input: n = 2
# Output: [0,1,1]
print(s.countBits(2))


# Input: n = 5
# Output: [0,1,1,2,1,2]
# print(s.countBits(5))
