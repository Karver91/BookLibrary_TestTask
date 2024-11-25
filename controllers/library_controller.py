import traceback

import logger
from services.library_service import BookService
from views.console_view import console


class BookController:
    """Обрабатывает команды, связанные с книгами"""
    def __init__(self, service: BookService):
        self.service = service

    def add_book(self) -> None:
        """Добавить книгу"""
        try:
            console.print_add_book_info()
            title, author, year = [
                console.user_input(msg) for msg in (
                    'Введите название книги: ',
                    'Введите автора книги: ',
                    'Введите год издания книги: '
                )
            ]
            book = self.service.add_book(title, author, year)
            console.print_book_message(book, 'Книга добавлена в библиотеку')
        except ValueError as e:
            console.print_exception_message(e)
            logger.log_exception(traceback.format_exc())

    def remove_book(self) -> None:
        """Удалить книгу"""
        try:
            console.print_remove_book_info()
            book_id = console.user_input()
            book = self.service.remove_book(book_id)
            console.print_book_message(book, 'Книга удалена из библиотеки')
        except ValueError as e:
            console.print_exception_message(e)
            logger.log_exception(traceback.format_exc())


    def search_book(self) -> None:
        """Ищет книги по их названию, автору или году издания"""
        console.print_search_book_info()
        user_input = console.user_input()
        result = self.service.search_book(user_input)
        console.print_books(result)

    def print_all_books(self) -> None:
        """Выводит все доступные книги на экран"""
        console.print_books(self.service.file_manager.data)

    def change_book_status(self) -> None:
        """Изменить статус книги"""
        try:
            console.print_change_book_status_info()
            book_id = console.user_input()
            book = self.service.get_obj_by_id(book_id)
            if not book:
                console.print_book_not_found()
                return
            console.print_book_message(book, 'Найдена книга')
            self.service.change_book_status(book)
            console.print_book_message(book, 'Статус изменен')
        except ValueError as e:
            console.print_exception_message(e)
            logger.log_exception(traceback.format_exc())