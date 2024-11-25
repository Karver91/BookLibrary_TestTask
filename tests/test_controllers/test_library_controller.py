import copy
from unittest.mock import patch

import pytest

from enums import BookStatusEnum
from views.console_view import console


class TestBookController:
    def test_add_book(self, book_controller):
        title = 'some_title'
        author = 'some_author'
        year = '1999'
        msg = 'Книга добавлена в библиотеку'

        with patch('builtins.print') as mock_print:
            console.print_message(msg)
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=[title, author, year]):
                # Вызываем метод
                book_controller.add_book()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)

    def test_remove_book(self, book_controller):
        book = book_controller.service.file_manager.data[0]
        msg = 'Книга удалена из библиотеки'

        with patch('builtins.print') as mock_print:
            console.print_message(msg)
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=[book.id]):
                # Вызываем метод
                book_controller.remove_book()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)

    def test_search_book(self, book_controller):
        book = book_controller.service.file_manager.data[0]

        with patch('builtins.print') as mock_print:
            console.print_books([book])
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=[book.title]):
                # Вызываем метод
                book_controller.search_book()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)

    def test_print_all_books(self, book_controller):
        books = book_controller.service.file_manager.data
        with patch('builtins.print') as mock_print:
            console.print_books(books)
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            # Вызываем метод
            book_controller.print_all_books()
            # Проверяем вывод на экран
            mock_print.assert_any_call(expected_result)

    def test_change_book_status(self, book_controller):
        book = book_controller.service.file_manager.data[0]
        copy_book = copy.copy(book)
        copy_book.status = BookStatusEnum.CHECKED_OUT.value
        with patch('builtins.print') as mock_print:
            console.print_book_message(copy_book, 'Статус изменен')
            expected_result = mock_print.call_args.args[0]

        with patch('builtins.print') as mock_print:
            with patch('builtins.input', side_effect=[book.id, '2']):
                # Вызываем метод
                book_controller.change_book_status()
                # Проверяем вывод на экран
                mock_print.assert_any_call(expected_result)
