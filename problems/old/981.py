from collections import defaultdict

import bisect


class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""

        timestaps = self.data[key]

        # idx = bisect.bisect_right(timestaps, timestamp, key=lambda a: a[0])

        l, r = 0, len(timestaps) - 1

        while l < r:
            mid = (l + r) // 2

            if timestaps[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if r <= 0:
            return ""

        return timestaps[r - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


timeMap = TimeMap()
# timeMap.set("foo", "bar", 1)
# # store the key "foo" and value "bar" along with timestamp = 1.
# print(timeMap.get("foo", 1))
# # return "bar"
# print(timeMap.get("foo", 3))
# # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4)
# # store the key "foo" and value "bar2" along with timestamp = 4.
# print(timeMap.get("foo", 4))
# # return "bar2"
# print(timeMap.get("foo", 5))
# # return "bar2"

# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# [null,null,null,"","high","high","low","low"]
timeMap.set("love", "high", 10)
timeMap.set("love", "low", 20)

# "",
print(timeMap.get("love", 5))
# "high"
print(timeMap.get("love", 10))
# ,"high"
print(timeMap.get("love", 15))
# ,"low",
print(timeMap.get("love", 20))
# "low"
print(timeMap.get("love", 25))
