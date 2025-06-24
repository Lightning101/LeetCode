from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans["".join(sorted(s))].append(s)

        return list(ans.values())


s = Solution()


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Example 2:

# Input: strs = [""]

# Output: [[""]]

print(s.groupAnagrams([""]))

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

print(s.groupAnagrams(["a"]))
