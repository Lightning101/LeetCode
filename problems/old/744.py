class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        l, r = -1, len(letters)

        while l < r:
            mid = (l + r) // 2
            if ord(target) > ord(letters[mid]):
                l = mid + 1
            else:
                r = mid - 1

        if -1 < l < len(letters):
            return letters[l]

        return letters[0]


s = Solution()


print(s.nextGreatestLetter(["c", "f", "j"], "k"))
