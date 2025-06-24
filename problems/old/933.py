from collections import deque
class RecentCounter:

    def __init__(self):
        self.data = deque()

    def ping(self, t: int) -> int:
        self.data.append(t)
        llimit = t - 3000

        while(self.data and self.data[0] < llimit):
            self.data.popleft()
        return len(self.data)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
