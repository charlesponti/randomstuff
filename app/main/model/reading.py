class ReadingItem(object):
    word_length: int
    content: str

    def __init__(self, *args, word_length=0, content: str = None):
        self.word_length = word_length
        self.content = content


class Article(ReadingItem):
    def __init__(self, *args, word_length=0, content=None):
        super().__init__(*args, word_length=word_length, content=content)


class Book(ReadingItem):
    def __init__(self, *args, word_length=0, content=None):
        super().__init__(*args, word_length=word_length, content=content)
