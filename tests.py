import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name, book_genre',
                             [['Майор', 'Детективы'], ['Коты', 'Комедии'], ['Мурзик', 'Мультфильмы']])
    def test_set_book_genre_if_book_have_books_genre_and_book_genre_have_genre(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre().get(book_name) == book_genre

    @pytest.mark.parametrize('new_book', ['Что делать, если ваш кот хочет вас убить', 'Фиксики', 'Турбозавры'])
    def test_get_book_genre_in_book_name(self, new_book):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        book_name = ''

        for key in collector.get_books_genre():
            book_name = key

        assert book_name == new_book

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Земля')
        collector.set_book_genre('Земля', 'Ужасы')

        collector.add_new_book('Марс')
        collector.set_book_genre('Марс', 'Ужасы')

        collector.add_new_book('Волк одинкочка')
        collector.set_book_genre('Волк одинкочка', 'Детективы')

        collector.add_new_book('Майор')
        collector.set_book_genre('Майор', 'Детективы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Волк одинкочка', 'Майор']

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Земля')
        collector.add_new_book('Марс')
        collector.add_new_book('Волк одинкочка')
        collector.add_new_book('Майор')

        assert collector.get_books_genre() == {'Земля': '', 'Марс': '', 'Волк одинкочка': '', 'Майор': ''}

    def test_get_books_for_children_if_not_genre_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Земля')
        collector.set_book_genre('Земля', 'Ужасы')

        collector.add_new_book('Майор')
        collector.set_book_genre('Майор', 'Фантастика')

        collector.add_new_book('Дядя Коля')
        collector.set_book_genre('Дядя Коля', 'Мультфильмы')

        collector.add_new_book('Мурзилка')
        collector.set_book_genre('Мурзилка', 'Комедии')

        assert collector.get_books_for_children() == ['Майор', 'Дядя Коля', 'Мурзилка']

    def test_add_book_in_favorites_in_books_genre_without_repeat(self):
        collector = BooksCollector()

        collector.add_new_book('Земля')
        collector.add_book_in_favorites('Земля')

        collector.add_new_book('Майор')
        collector.add_book_in_favorites('Майор')

        collector.add_new_book('Дядя Коля')
        collector.add_book_in_favorites('Дядя Коля')

        assert collector.favorites == ['Земля', 'Майор', 'Дядя Коля']

    @pytest.mark.parametrize('book_name', ['Земля', 'Мары', 'Transformers'])
    def test_delete_book_from_favorites_if_book_in_favorites(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Земля')
        collector.add_book_in_favorites('Земля')

        collector.add_new_book('Майор')
        collector.add_book_in_favorites('Майор')

        collector.add_new_book('Дядя Коля')
        collector.add_book_in_favorites('Дядя Коля')

        assert collector.get_list_of_favorites_books() == ['Земля', 'Майор', 'Дядя Коля']
