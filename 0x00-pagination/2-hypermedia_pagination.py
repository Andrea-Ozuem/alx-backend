#!/usr/bin/env python3
'Simple Pagination'

import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset
        (i.e. the correct list of rows)"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """return hyper media of a page"""
        all_p = len(self.dataset())
        remain = math.ceil(all_p / page_size)
        data = self.get_page(page, page_size)
        hyper = {'page_size': len(data), 'page': page, 'data': data,
                 'next_page': page + 1 if remain > page + 1 else None,
                 'prev_page': page - 1 if page > 1 else None,
                 'total_pages': remain}
        return hyper
