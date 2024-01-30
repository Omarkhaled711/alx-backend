#!/usr/bin/env python3
"""
second task module
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function returns a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        a method named get_page that takes two integer arguments page with
        default value 1 and page_size with default value 10.
        and return the appropriate page of the dataset
        (i.e. the correct list of rows).
        """
        assert type(page_size) is int and page_size > 0
        assert type(page) is int and page > 0
        index = index_range(page, page_size)
        data = self.dataset()
        try:
            content = [data[i]
                       for i in range(index[0], index[1])]
            return content
        except IndexError:
            return []
