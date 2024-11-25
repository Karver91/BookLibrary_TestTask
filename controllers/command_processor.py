from controllers.library_controller import BookController
from views.console_view import console


class CommandProcessor:
    def __init__(self, book_controller: BookController):
        self.book_controller = book_controller
        self.commands = {
            'help': {'method': self.help_command, 'description': 'Выводит список команд на экран'},
            'exit': {'method': self.exit_command, 'description': 'Выход из приложения'},
            '1': {'method': self.book_controller.add_book, 'description': 'Добавить книгу в библиотеку'},
            '2': {'method': self.book_controller.remove_book, 'description': 'Удалить книгу из библиотеки'},
            '3': {'method': self.book_controller.search_book, 'description': 'Найти книгу в библиотеке'},
            '4': {'method': self.book_controller.print_all_books, 'description': 'Показать все книги'},
            '5': {'method': self.book_controller.change_book_status, 'description': 'Изменение статуса книги'}
        }

    def process_command(self, command: str) -> None:
        if command in self.commands:
            self.commands[command]['method']()
        else:
            console.print_message(f"Неизвестная команда: {command}. Введите 'help' для списка команд.")

    def help_command(self) -> None:
        console.print_command_info(self.commands)

    def exit_command(self) -> None:
        console.print_exit_command_info()
        exit()

    def run(self):
        try:
            console.print_welcome_message()
            console.print_command_info(self.commands)
            while True:
                user_input = console.user_input('\nЧтобы увидеть список команд введите "help"\nВведите команду: ').lower()
                self.process_command(user_input)
        except KeyboardInterrupt:
            console.print_message('Работа программы завершена')
            exit()

