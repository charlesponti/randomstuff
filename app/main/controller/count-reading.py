from typing import List

from app.main.model.reading import Article, Book

# Book pages have 250-300 words per page
WORDS_PER_PAGE = 275

# the average adult reads 250 words per minute
WORDS_PER_MINUTE = 250


class Reading:
    def __init__(self):
        # articles that have been read
        self.read: List = []
        # articles that user wants to read
        self.reading: List = []

    def get_amount_to_read(self):
        count = 0

        for item in self.reading_list:
            count += item.word_length / 250

        return count

    def get_reading_count(self):
        return len(self.read)
