#!/usr/bin/env python3

# First in First out caching

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.lookup = set()


    def access(self, item):# Adds an item to the cache, if the cache is full it removes the oldest item to make space
        if item not in self.lookup:
            if len(self.cache) >= self.capacity:
                removed = self.cache.pop(0)
                self.lookup.remove(removed)
            self.cache.append(item)
            self.lookup.add(item)

        print(f"Cache: {self.cache}")


# Example usage
fifo_cache = FIFOCache(3)
fifo_cache.access('a')
fifo_cache.access('b')
fifo_cache.access('c')
fifo_cache.access('d')
