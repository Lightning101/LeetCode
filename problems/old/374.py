


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        mid = n // 2
        found = False
        while not found:
            res = guess(mid)
            if res == 0:
                found = True
            elif res < 0:
                mid = mid // 2
            else:
                mid = (mid + 1 + n) // 2

        return mid
