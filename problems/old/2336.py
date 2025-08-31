
# Heap set implementation
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.removeEle = set()

    def findNextSmallestEle(self):
        heap = list(self.removeEle)
        heapq.heapify(heap)

        if heap and heap[0] - 1 > 0:
            return heap[0] - 1

        counter = heap[0] if heap else 1
        while counter in self.removeEle:
            counter += 1

        return counter

    def popSmallest(self) -> int:

        ele = self.findNextSmallestEle()
        self.removeEle.add(ele)
        return ele

    def addBack(self, num: int) -> None:
        if num in self.removeEle:
            self.removeEle.remove(num)

# SortedSet implmentation

# from sortedcontainers import SortedSet


# class SmallestInfiniteSet:

#     def __init__(self):
#         self.removeEle = SortedSet()
#         self.counter = 1

#     def popSmallest(self) -> int:
#         if self.removeEle and self.counter >= self.removeEle[0]:
#             while self.counter in self.removeEle:
#                 self.counter += 1

#         ans = self.counter
#         self.counter += 1
#         self.removeEle.add(ans)
#         return ans

#     def addBack(self, num: int) -> None:
#         if num in self.removeEle:
#             self.removeEle.remove(num)
#             if self.counter >= num:
#                 self.counter = num

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


# Example 1:

# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]

# Explanation
smallestInfiniteSet = SmallestInfiniteSet()
smallestInfiniteSet.addBack(2)  # 2 is already in the set, so no change is made.
print(
    smallestInfiniteSet.popSmallest()
)  # return 1, since 1 is the smallest number, and remove it from the set.
print(smallestInfiniteSet.popSmallest())  # return 2, and remove it from the set.
print(smallestInfiniteSet.popSmallest())  # return 3, and remove it from the set.
smallestInfiniteSet.addBack(1)  # 1 is added back to the set.
print(
    smallestInfiniteSet.popSmallest()
)  # return 1, since 1 was added back to the set and
# is the smallest number, and remove it from the set.
print(smallestInfiniteSet.popSmallest())  # return 4, and remove it from the set.
print(smallestInfiniteSet.popSmallest())  # return 5, and remove it from the set.
