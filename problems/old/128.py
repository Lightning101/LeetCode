class Solution:
    def longestConsecutive(self, nums) -> int:
        mem = set()

        for i in nums:
            if not i in mem:
                mem.add(i)

        ans = 0
        keys = list(mem)
        for key in keys:
            if key in mem:
                count = 1
                start = key - 1
                while start in mem:
                    count += 1
                    # del mem[start]
                    mem.discard(start)
                    start -= 1

                end = key + 1
                while end in mem:
                    count += 1
                    mem.discard(end)
                    # del mem[end]
                    end += 1

                if count > ans:
                    ans = count

        return ans


s = Solution()


nums = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(nums))
