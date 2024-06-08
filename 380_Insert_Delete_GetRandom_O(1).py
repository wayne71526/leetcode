# solution
class RandomizedSet:

    def __init__(self):
        self.unique_item = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.unique_item:
            return False

        self.unique_item.append(val)
        self.index[val] = len(self.unique_item) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.unique_item:
            return False

        idx = self.index[val]
        last = self.unique_item[idx] = self.unique_item[-1]  # 將最後一個元素移到 idx
        self.index[last] = idx                               # 移完後將其 index 做更改
        self.unique_item.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.unique_item)