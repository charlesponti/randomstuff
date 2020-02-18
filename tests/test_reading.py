import pytest

from app.main.model.reading import Article, Book


@pytest.fixture
def article():
    return (Article(word_length=250),)


@pytest.fixture
def book():
    return Book(title="All Quiet on the Western Front", word_length=75000)
