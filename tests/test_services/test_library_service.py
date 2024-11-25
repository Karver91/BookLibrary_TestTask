from unittest.mock import patch

import pytest

from models.library_models import Book
from services.library_service import BookService


class TestAddBook:
    def test_add_book(self, book_service: BookService):
        title = 'test_title_2'
        author = 'test_author'
        year = '1999'
        amount_database_obj = len(book_service.file_manager.data)

        # Вызываем метод
        result = book_service.add_book(title, author, year)
        amount_database_obj += 1

        # Ассерты
        assert isinstance(result, Book), 'Возвращаемый результат должен принадлежать модели Book'
        assert result in book_service.file_manager.data, 'В базе не найден объект новый объект Book'
        assert amount_database_obj == len(book_service.file_manager.data), \
            'Величина базы не соответствует ожидаемому значению'


    @pytest.mark.parametrize(
        'title, author, year, expected_result',
        [
            ('', 'some_author', '1999', 'Поля не заполнены'),
            ('some_title', 'author_12345', '1999', 'Поле Автор не должно содержать чисел'),
            ('some_title', 'some_author', 'sfasf', 'Год издания должен быть числом'),
            ('some_title', 'some_author', '9999', 'Год издания должен быть меньше текущего')
        ]
    )
    def test_exception(self, book_service: BookService,
                       title, author, year, expected_result):
        database = book_service.file_manager.data[:].sort()

        # Вызываем метод
        with pytest.raises(ValueError) as exc_info:
            book_service.add_book(title, author, year)

        # Ассерты
        assert str(exc_info.value) == expected_result
        assert database == book_service.file_manager.data.sort(), 'Данные в базе не должны были изменяться'


class TestRemoveBook:
    def test_remove_book(self, book_service: BookService):

        amount_database_obj = len(book_service.file_manager.data)
        book = book_service.file_manager.data[0]

        # Вызываем метод
        result = book_service.remove_book(book.id)
        amount_database_obj -= 1

        # Ассерты
        assert result == book, 'Метод должен вернуть удаляемый объект'
        assert book not in book_service.file_manager.data, 'Объект не должен присутствовать в базе'


    @pytest.mark.parametrize(
        'book_id, expected_result',
        [
            (-1, 'Книга не найдена в базе'),
            ('', 'Неверно переданные данные')
        ]
    )
    def test_exception(self, book_service: BookService,
                       book_id, expected_result):
        database = book_service.file_manager.data[:].sort()

        # Вызываем метод
        with pytest.raises(ValueError) as exc_info:
            book_service.remove_book(book_id)

        # Ассерты
        assert str(exc_info.value) == expected_result
        assert database == book_service.file_manager.data.sort(), 'Данные в базе не должны были изменяться'


class TestSearchBook:
    def test_search_book(self, book_service):
        book = book_service.file_manager.data[0]

        title = book.title
        author = book.author
        year = book.year

        # Вызываем метод
        result = book_service.search_book(title)
        assert book in result, 'Книга не найдена по названию'
        result = book_service.search_book(author)
        assert book in result, 'Книга не найдена по автору'
        result = book_service.search_book(year)
        assert book in result, 'Книга не найдена по году издания'


class TestChangeBookStatus:
    def test_change_book_status(self, book_service):
        book = book_service.file_manager.data[0]
        book_status = book.status

        # Вызываем метод
        with patch('builtins.input', side_effect=['2']):
            result = book_service.change_book_status(book)

        assert result.status != book_status, 'Статус не изменился'
