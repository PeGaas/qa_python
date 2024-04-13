from main import BooksCollector
import pytest


@pytest.fixture()
def books_collector():
    collector = BooksCollector()
    return collector
