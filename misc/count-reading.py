
# Book pages have 250-300 words per page
WORDS_PER_PAGE = 275

# the average adult reads 250 words per minute
WORDS_PER_MINUTE = 250

class Article(object):
    word_length: int
    content: str

    def __init__(self, word_length=0,content=''):
        self.word_length = word_length
        self.content = content

# articles that have been read
reading_list = [
    Article(word_length=250),
    Book(title=, word_length=75000)
]


# articles that have been read
read = [

]

def get_amount_to_read():
    count = 0

    for article in reading_list:
        count += (article.word_length / 250)

    return count

def get_reading_count():
    return True

