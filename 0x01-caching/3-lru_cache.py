#!/usr/bin/env python3
'''0. Basic dictionary'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''a caching system'''
    def __init__(self):
        '''Initiliaze'''
        super().__init__()
        self.key_index = {}
        self.count = 0

    def put(self, key, item):
        '''assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key and item:
            if key in self.cache_data:
                self.count += 1
                self.key_index.update({key: self.count})
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # discard lru item
                min_val = min(self.key_index.values())
                min_key = [key for key in self.key_index
                           if self.key_index[key] == min_val][0]
                self.cache_data.pop(min_key)
                del self.key_index[min_key]
                print('DISCARD: {}'.format(min_key))
            self.cache_data[key] = item
            self.count += 1
            self.key_index.update({key: self.count})

    def get(self, key):
        '''return the value in self.cache_data linked to key
        '''
        if key in self.cache_data:
            self.count += 1
            self.key_index.update({key: self.count})
            return self.cache_data.get(key)
