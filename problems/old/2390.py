from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        st = deque()

        for c in s:
            if(c == '*'):
                st.pop()
            else:
                st.append(c)
        return ''.join(st)
        