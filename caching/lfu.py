#!/usr/bin/env python3
# Least Frequently used caching property

from collections import Counter

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = Counter()

    def access(self, item):# Adds an item to the cache. If the cache is full, it removes the least frequency used item to make space
        if item in self.cache:
            self.freq[item] += 1
        else:
            if len(self.cache) >= self.capacity:
                lfu_item = min(self.freq, key=self.freq.get)
                del self.cache[lfu_item]
                del self.freq[lfu_item]
            self.cache[item] = True
            self.freq[item] = 1

        print(f"Cache: {list(self.cache.keys())}")


# Example in use
lfu_cache = LFUCache(3)
lfu_cache.access('a')
lfu_cache.access('b')
lfu_cache.access('c')
lfu_cache.access('a')
lfu_cache.access('b')
lfu_cache.access('d')
