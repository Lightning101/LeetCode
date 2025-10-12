# import random


# class RandomizedSet:

#     def __init__(self):
#         self.data = {}
#         self.og = 0

#     def insert(self, val: int) -> bool:
#         exists = not val in self.data
#         self.data[val] = val
#         return exists

#     def remove(self, val: int) -> bool:
#         if val in self.data:
#             del self.data[val]
#             return True
#         return False

#     def getRandom(self) -> int:
#         iterfunc = iter if (self.og) else reversed
#         it = iterfunc(self.data.keys())
#         idx = random.randrange(0, min(self.maxRand, len(self.data)))
#         for _ in range(idx):
#             next(it)
#         return next(it)


import random


class RandomizedSet:

    def __init__(self):
        self.keyMap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.keyMap[val] = len(self.data)
        self.data.append(val)

    def remove(self, val: int) -> bool:
        if val in self.keyMap:
            self.data[self.keyMap[val]], self.data[-1] = (
                self.data[-1],
                self.data[self.keyMap[val]],
            )
            self.keyMap[self.data[self.keyMap[val]]] = self.keyMap[val]
            del self.keyMap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
randomizedSet = RandomizedSet()
randomizedSet.insert(
    1
)  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2)  # Returns false as 2 does not exist in the set.
randomizedSet.insert(2)  # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom())  # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1)  # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2)  # 2 was already in the set, so return false.
print(
    randomizedSet.getRandom()
)  # Since 2 is the only number in the set, getRandom() will always return 2.
