from collections import deque


# class Solution:
#     def decodeString(self, s: str) -> str:
#         st = deque()

#         for c in s:
#             if (
#                 c.isalnum()
#                 and st
#                 and st[-1].isalnum()
#                 and st[-1].isnumeric() == c.isnumeric()
#             ):
#                 st[-1] += c
#             else:
#                 st.append(c)

#         ans = ""
#         while st:
#             op = 1
#             if st[0].isnumeric():
#                 op = int(st.popleft())

#             if st[0] == "[":
#                 # Find contents of brackets
#                 bk = deque()
#                 bk.append(st.popleft())
#                 eles = []
#                 complex_ele = False
#                 while bk:
#                     ele = st.popleft()
#                     if ele in "[]":
#                         if bk[-1] == "[" and ele == "]":
#                             bk.pop()
#                             if bk:
#                                 # Contains Inner Brackets
#                                 complex_ele = True
#                         else:
#                             bk.append(ele)
#                     eles.append(ele)

#                 eles.pop()
#                 # Check if elements are not complex then directly to answer
#                 if not complex_ele:
#                     ans += "".join(eles) * op
#                 else:
#                     # Added it back to the stack after expainsion
#                     st = deque(eles * op) + st
#             else:
#                 # If not a complex element add to answer
#                 ans += st.popleft() * op

#         return ans


class Solution:
    def decodeString(self, s: str) -> str:
        st = deque()
        for c in s:
            if c == "]":

                ct = ""
                while st[-1] != "[":
                    ct += st.pop()

                st.pop()
                op = ""
                while st and st[-1].isnumeric():
                    op = st.pop() + op

                st.extend(ct[::-1] * int(op))
            else:
                st.append(c)
        return "".join(st)


s = Solution()


# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

print(s.decodeString("3[a]2[bc]"))
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
print(s.decodeString("3[a2[c]]"))
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
print(s.decodeString("2[abc]3[cd]ef"))


# "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
