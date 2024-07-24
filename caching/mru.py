#!/usr/bin/env python3
# Most recently used caching property

class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def access(self, item):
        if item in self.cache:
            self.cache.remove(item)
        elif len(self.cache) >= self.capacity:
            self.cache.pop()
        self.cache.append(item)
        print(f"Cache: {self.cache}")


# Example in use
mru_cache = MRUCache(3)
mru_cache.access('a')
mru_cache.access('b')
mru_cache.access('c')
mru_cache.access('d')
