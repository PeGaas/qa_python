import pytest


class TestBooksCollector:
    @pytest.mark.parametrize('book_name_one', ['King Of Artur', 'Spider-Man'])
    def test_add_new_book_add_one_book(self, books_collector, book_name_one):
        books_collector.add_new_book(book_name_one)

        assert len(books_collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ['', 'Волшебный лес: путешествие в мир чудес и загадок'])
    def test_add_new_book_name_length_more_then41_or_zero(self, books_collector, book_name):
        books_collector.add_new_book(book_name)

        assert books_collector.get_books_genre() == {}

    @pytest.mark.parametrize('book_name, book_genre',
                             [['Майор', 'Детективы'], ['Коты', 'Комедии'], ['Мурзик', 'Мультфильмы']])
    def test_set_book_genre_if_book_have_books_genre_and_book_genre_have_genre(self, book_name, book_genre,
                                                                               books_collector):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)

        assert books_collector.get_books_genre().get(book_name) == book_genre

    @pytest.mark.parametrize('new_book', ['Что делать, если ваш кот хочет вас убить', 'Фиксики', 'Турбозавры'])
    def test_get_book_genre_in_book_name(self, new_book, books_collector):
        books_collector.add_new_book(new_book)
        book_name = ''

        for key in books_collector.get_books_genre():
            book_name = key

        assert book_name == new_book

    @pytest.mark.parametrize('book_name, book_genre', [['Земля', 'Ужасы'], ['Марс', 'Ужасы'], ['Майор', 'Детективы']])
    def test_get_books_with_specific_genre(self, book_name, book_genre, books_collector):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)

        assert books_collector.get_books_with_specific_genre(book_genre) == [book_name]

    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book('Земля')
        books_collector.add_new_book('Марс')
        books_collector.add_new_book('Волк одинкочка')
        books_collector.add_new_book('Майор')

        assert books_collector.get_books_genre() == {'Земля': '', 'Марс': '', 'Волк одинкочка': '', 'Майор': ''}

    def test_get_books_for_children_if_not_genre_age_rating(self, books_collector):
        books_collector.add_new_book('Земля')
        books_collector.set_book_genre('Земля', 'Ужасы')

        books_collector.add_new_book('Майор')
        books_collector.set_book_genre('Майор', 'Фантастика')

        books_collector.add_new_book('Дядя Коля')
        books_collector.set_book_genre('Дядя Коля', 'Мультфильмы')

        books_collector.add_new_book('Мурзилка')
        books_collector.set_book_genre('Мурзилка', 'Комедии')

        assert books_collector.get_books_for_children() == ['Майор', 'Дядя Коля', 'Мурзилка']

    def test_add_book_in_favorites_in_books_genre_without_repeat(self, books_collector):
        books_collector.add_new_book('Земля')
        books_collector.add_book_in_favorites('Земля')

        books_collector.add_new_book('Майор')
        books_collector.add_book_in_favorites('Майор')

        books_collector.add_new_book('Дядя Коля')
        books_collector.add_book_in_favorites('Дядя Коля')

        assert books_collector.favorites == ['Земля', 'Майор', 'Дядя Коля']

    @pytest.mark.parametrize('book_name', ['Земля', 'Мары', 'Transformers'])
    def test_delete_book_from_favorites_if_book_in_favorites(self, book_name, books_collector):
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)

        assert book_name not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book('Земля')
        books_collector.add_book_in_favorites('Земля')

        books_collector.add_new_book('Майор')
        books_collector.add_book_in_favorites('Майор')

        books_collector.add_new_book('Дядя Коля')
        books_collector.add_book_in_favorites('Дядя Коля')

        assert books_collector.get_list_of_favorites_books() == ['Земля', 'Майор', 'Дядя Коля']
