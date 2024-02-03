#!/usr/bin/env python3
"""second task module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Implementing a LRU Cache """

    def __init__(self):
        """
        Define an init method for LRU Cache
        """
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value
        for the key key.If key or item is None, this method should
        not do anything. If the number of items in self.cache_data is
        higher that BaseCaching.MAX_ITEMS. Discard the least recently
        used item put in cache (LRU algorithm)
        """
        if key is not None and item is not None:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.__queue[0]))
                del self.cache_data[self.__queue[0]]
                del self.__queue[0]
            if key in self.__queue:
                del self.__queue[self.__queue.index(key)]
            self.__queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is not None and key in self.cache_data.keys():
            del self.__queue[self.__queue.index(key)]
            self.__queue.append(key)
            return self.cache_data[key]
        return None
