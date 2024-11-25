import traceback

from data_managment.file_manager import BaseFileManager
from enums import BookStatusEnum
from models.library_models import Book
from views.console_view import console


class BaseService:
    def __init__(self, file_manager: BaseFileManager):
        self.file_manager = file_manager

    def get_obj_by_id(self, obj_id) -> Book | None:
        """Возвращает объект из data по его id"""
        try:
            obj_id = int(obj_id)
            result = None
            for obj in self.file_manager.data:
                if obj.id == obj_id:
                    result = obj
                    break
            return result
        except ValueError as e:
            raise ValueError('Неверно переданные данные')


    @staticmethod
    def user_input_command(commands):
        """Просит пользователя ввести команду из списка команд"""
        while True:
            user_input = console.user_input()
            if not user_input in commands.keys():
                console.print_message("Введена неверная команда. Попробуйте еще раз")
                continue
            break
        return user_input

    @staticmethod
    def get_all_enum_statuses(enum_obj) -> list[tuple]:
        """Возвращает статусы объекта enum"""
        result = list()
        for name, member in enum_obj.__members__.items():
            result.append((name, member))
        return result


class BookService(BaseService):
    def __init__(self, file_manager: BaseFileManager):
        super().__init__(file_manager)
        
    def add_book(self, title: str, author: str, year: str) -> Book | None:
        try:
            book_id = self.file_manager.generate_id()
            new_book = Book(book_id, title, author, year)
            self.file_manager.add_data_obj(new_book)
            return new_book
        except ValueError:
            raise

    def remove_book(self, book_id):
        try:
            book = self.get_obj_by_id(book_id)
            if not book in self.file_manager.data:
                raise ValueError('Книга не найдена в базе')
            self.file_manager.remove_data_obj(book)
            return book
        except ValueError:
            raise


    def search_book(self, user_input: str) -> list[Book]:
        """Ищет книги по их названию, автору или году издания"""
        books = [book for book in self.file_manager.data if user_input in (book.title, book.author, book.year)]
        return books

    def change_book_status(self, book: Book):
        try:
            commands = self.get_status_commands()
            console.print_command_info(commands)
            user_input = self.user_input_command(commands)
            status = commands[user_input]['description']
            book.status = status
            return book
        except ValueError:
            raise

    def get_status_commands(self):
        book_statuses = self.get_all_enum_statuses(BookStatusEnum)
        status_values = [x[1].value for x in book_statuses]
        commands = {str(key): {'description': value} for key, value in enumerate(status_values, start=1)}
        return commands