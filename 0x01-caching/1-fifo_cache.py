#!/usr/bin/env python
"""FIFO"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Assign the item value to the key in self.cache_data.
        If the number of items exceeds BaseCaching.MAX_ITEMS,
        discard the first item (FIFO algorithm).
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}\n")

    def get(self, key):
        """
        Return the value associated with the key in self.cache_data.
        If key is None or doesn't exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
