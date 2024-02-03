#!/usr/bin/env python3
"""second task module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Implementing a FIFO Cache """

    def __init__(self):
        """
        Define an init method for LIFO Cache
        """
        super().__init__()
        self.__stack = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value
        for the key key.If key or item is None, this method should
        not do anything. If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS. Discard the last item put in
        cache (LIFO algorithm)
        """
        if key is not None and item is not None:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.__stack[-1]))
                del self.cache_data[self.__stack[-1]]
                del self.__stack[-1]
            if key in self.__stack:
                del self.__stack[self.__stack.index(key)]
            self.__stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
