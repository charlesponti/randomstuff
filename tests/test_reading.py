import pytest

from app.main.model.reading import Article, Book


@pytest.fixture
def article():
    return (Article(word_length=250),)


@pytest.fixture
def book():
    return Book(title="All Quiet on the Western Front", word_length=75000)


@pytest.mark.parametrize("title,no_title", [("Foo Bar", None)])
def test_articles(title, no_title):
    book_with_title = Book(title=title)
    book_with_no_title = Book(title=no_title)
    assert book_with_no_title.title == None
    assert book_with_title.title == title
