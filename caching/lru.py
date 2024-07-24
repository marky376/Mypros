#!/usr/bin/env python3
# Least Recently Used caching property

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
    def access(self, item):# Adds an item to the cache. if the cache is full, it removes the least recently used item to make space
        if item in self.cache:
            self.cache.remove(item)
        elif len(self.cache) >= self.capacity:
            self.cache.pop(0)
        self.cache.append(item)
        print(f"Cache: {self.cache}")


# Example usage
lru_cache = LRUCache(3)
lru_cache.access('a')
lru_cache.access('b')
lru_cache.access('c')
lru_cache.access('a')
lru_cache.access('d')
