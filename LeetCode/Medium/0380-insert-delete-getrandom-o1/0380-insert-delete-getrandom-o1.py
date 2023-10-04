from random import choice

class RandomizedSet:
    def __init__(self):
        self.rand_set = {}

    def insert(self, val: int) -> bool:
        if val in self.rand_set:
            return False
        self.rand_set[val] = 0
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rand_set:
            return False
        del self.rand_set[val]
        return True

    def getRandom(self) -> int:
        return choice(list(self.rand_set.keys()))