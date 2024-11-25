import traceback

import logger
from controllers.command_processor import CommandProcessor
from config import settings
from controllers.library_controller import BookController
from data_managment.file_manager import JSONFileManager
from models.library_models import Book
from services.library_service import BookService
from views.console_view import console


def main():
    file_manager = JSONFileManager(model=Book, data_path=settings.data_file_path)
    book_service = BookService(file_manager=file_manager)
    book_controller = BookController(service=book_service)
    processor = CommandProcessor(book_controller)
    processor.run()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.log_exception(traceback.format_exc())
        console.print_exception_message('Ошибка. Программа завершена')
