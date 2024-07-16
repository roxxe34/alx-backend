#!/usr/bin/env python3
"""Simple helper function"""

import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page, page_size):
    """start index and end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """
        get page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        i = index_range(page, page_size)
        data = self.dataset()
        if i is None:
            return []
        return data[i[0]:i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict[str, Any]:
        """
        Return dataset as a dictionary
        """
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        pagination = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(),
            'next_page': page + 1 if page + 1 <= total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return pagination
