from collections import Counter


# class Solution:
#     def compress(self, chars: list[str]) -> int:

#         counter = 0
#         original_size = len(chars)
#         processed = 0
#         lastEle = chars[0]

#         while processed < original_size:
#             if lastEle == chars[0]:
#                 counter += 1
#                 chars = chars[1:]
#                 processed += 1
#             else:
#                 chars.append(lastEle)
#                 if counter > 1:
#                     chars.extend([*str(counter)])
#                 counter = 0
#                 lastEle = chars[0]

#         chars.append(lastEle)
#         if counter > 1:
#             chars.extend([*str(counter)])

#         return len(chars)


# class Solution:
#     def compress(self, chars: list[str]) -> int:
#         p1, p2 = 0, 0
#         counter = 0
#         original_size = len(chars)

#         while p2 < original_size + 1:
#             if p2 == original_size or chars[p1] != chars[p2]:
#                 chars.append(chars[p1])
#                 if counter > 1:
#                     chars.extend([*str(counter)])
#                 counter = 0
#                 p1 = p2
#                 if p2 == original_size:
#                     break

#             else:
#                 counter += 1
#             p2 += 1

#         # chars.append(chars[p1])
#         # if counter > 1:
#         #     chars.extend([*str(counter)])

#         del chars[:original_size]


#         return len(chars)
class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        while i < len(chars):

            group_len = 0
            while i + group_len < len(chars) and chars[i + group_len] == chars[i]:
                group_len += 1

            if group_len > 1:
                str_rep = list(str(group_len))
                chars[i + 1 : i + group_len] = str_rep
                i += 1 + len(str_rep)
            else:
                i += 1
        return len(chars)   


s = Solution()


# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:
print(s.compress(["a"]))

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
