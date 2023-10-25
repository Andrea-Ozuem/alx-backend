#!/usr/bin/env python3
'''0. Basic dictionary'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''a caching system'''
    def __init__(self):
        '''Initiliaze'''
        super().__init__()

    def put(self, key, item):
        '''assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            self.cache_data.pop(first)
            print('DISCARD: {}'.format(first))
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key
        '''
        return self.cache_data.get(key)
