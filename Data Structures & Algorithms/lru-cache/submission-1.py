class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                item = self.cache.pop(i)
                self.cache.append(item)
                return item[1]

        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                item = self.cache.pop(i)
                item[1] = value
                self.cache.append(item)
                return
        
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        
        self.cache.append([key, value])
