# https://leetcode.com/problems/insert-delete-getrandom-o1
import random
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.values.append(val)
        self.map[val] = len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        lastValue = self.values[-1]
        # Swap last element with the element marked for deletion
        self.values[-1], self.values[index] = self.values[index], self.values[-1]
        self.map[lastValue] = index
        # Delete the element from list & map
        self.values.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()