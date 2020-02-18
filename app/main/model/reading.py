class ReadingItem(object):
    word_length: int
    content: str
    title: str

    def __init__(self, *args, word_length=0, content: str = None, title: str = None):
        self.word_length = word_length
        self.content = content
        self.title = title


class Article(ReadingItem):
    def __init__(self, *args, word_length=0, content=None, title: None):
        super().__init__(*args, word_length=word_length, content=content, title=title)


class Book(ReadingItem):
    def __init__(self, *args, word_length=0, content=None, title: None):
        super().__init__(*args, word_length=word_length, content=content, title=title)
