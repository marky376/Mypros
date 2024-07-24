#!/usr/bin/env python3
# Last in, First out caching

class LIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def access(self, item):# Adds an item to the cache. If the cache is full, it removes the most recently added item to make space
        if item not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.pop()
            self.cache.append(item)
        print(f"Cache: {self.cache}")

# Example in use
lifo_cache = LIFOCache(3)
lifo_cache.access('a')
lifo_cache.access('b')
lifo_cache.access('c')
lifo_cache.access('d')
