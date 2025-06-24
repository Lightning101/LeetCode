from collections import deque


class Solution:
    def asteroidCollision(self, asts: list[int]) -> list[int]:
        st = deque([asts[0]])

        for i in range(0, len(asts) - 1):
            idx = i + 1
            addStro = True
            if st and st[-1] > 0 and asts[idx] < 0:
                mag = abs(asts[idx])
                while st and st[-1] > 0 and asts[idx] < 0:
                    topMag = abs(st[-1])
                    if topMag < mag:
                        st.pop()
                    elif topMag >= mag:
                        if topMag == mag:
                            st.pop()
                        addStro = False
                        break

            if addStro:
                st.append(asts[idx])
        return list(st)


s = Solution()


print(s.asteroidCollision([-2, -2, 1, -2]))
print(s.asteroidCollision([5, 10, -5]))
print(s.asteroidCollision([-2, 1, 1, -1]))
print(s.asteroidCollision([1, -1, -2, -2]))
