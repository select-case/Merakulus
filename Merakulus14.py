class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)  
            self.cache[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            if len(self.cache) == self.capacity:
                LRU_keys = self.cache.keys()
                LRU_key = list(LRU_keys)[0]
                del self.cache[LRU_key]
        else:
            self.cache.pop(key)
        self.cache[key] = value