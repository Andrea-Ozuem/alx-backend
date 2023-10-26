#!/usr/bin/env python3
'''0. Basic dictionary'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''a caching system'''
    def __init__(self):
        '''Initiliaze'''
        super().__init__()
        self.key_index = []

    def put(self, key, item):
        '''assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            if len(self.cache_data) >= self.MAX_ITEMS:
                rm = self.cache_data.popitem()
                print('DISCARD: {}'.format(rm[0]))
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key
        '''
        return self.cache_data.get(key)
