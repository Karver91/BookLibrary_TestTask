import datetime

from config import settings


class BookView:
    """Отвечает за вывод данных в консоль"""

    @staticmethod
    def print_message(message: str):
        """Выводит сообщение в консоль"""
        print(f'\n{message}')

    @staticmethod
    def print_exception_message(message: str):
        """Выводит сообщение об ошибке"""
        msg_format = f'!!!{message}!!!'
        msg_len: int = len(msg_format) if len(msg_format) < 100 else 100
        print(f'\n{"-" * msg_len}\n{msg_format}\n{"-" * msg_len}')

    @staticmethod
    def print_book_info(_id, title, author, year, status):
        """Выводит информацию о книге"""
        print(
            f"{_id:<5} {title:<30} {author:<20} {year:<10} {status:<15}"
        )

    def print_book_not_found(self):
        self.print_message('Книг не найдено')

    def print_book_message(self, book, message):
        """Выводит переданное сообщение и информацию о книге"""
        if not book:
            self.print_book_not_found()
            return
        self.print_message(message)
        self.print_book_info('ID:', 'Название книги:', 'Автор:', 'Год:', 'Статус:')
        self.print_book_info(book.id, book.title, book.author, book.year, book.status)

    def print_books(self, books: list):
        """Выводит список книг"""
        if not books:
            self.print_book_not_found()
            return
        self.print_book_info('ID:', 'Название книги:', 'Автор:', 'Год:', 'Статус:')
        for book in books:
            self.print_book_info(book.id, book.title, book.author, book.year, book.status)

    def print_command_info(self, commands):
        """Выводит доступные команды"""
        self.print_message(f"Доступные команды: ")
        for key, value in commands.items():
            print(f'{key} - {value['description']}')

    def print_exit_command_info(self):
        self.print_message("Программа завершена")

    def print_add_book_info(self):
        self.print_message('Для добавления книги введите ее название, автора и год издания')

    def print_remove_book_info(self):
        self.print_message('Для удаления книги укажите ее id')

    def print_search_book_info(self):
        self.print_message('Введите название или автора или год издания книги для ее поиска')

    def print_change_book_status_info(self):
        self.print_message('Для изменения статуса книги введите ее ID')

    def print_welcome_message(self):
        """Выводит приветственное сообщение"""
        self.print_message('Добро пожаловать в нашу скромную библиотеку!\n'
                           'Элементом управления является набор простейших текстовых команд')

    @staticmethod
    def user_input(msg: str = 'Ввод: '):
        return input(msg)


console = BookView()
