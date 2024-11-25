import json

import pytest

from controllers.library_controller import BookController
from data_managment.file_manager import JSONFileManager
from enums import BookStatusEnum
from models.library_models import Book
from services.library_service import BookService


@pytest.fixture
def book_file_manager(tmp_path):
    """Фикстура для создания тестового JSON-файла."""
    # Создаем тестовый файл
    test_file = tmp_path / "test_data.json"
    file_manager = JSONFileManager(model=Book, data_path=test_file)

    test_data = Book(
        id=1,
        title='test_title_1',
        author='some_author',
        year='1999',
        status=BookStatusEnum.AVAILABLE.value
    )

    file_manager.add_data_obj(test_data)

    yield file_manager


@pytest.fixture
def book_service(book_file_manager):
    service = BookService(
        file_manager=book_file_manager
    )

    yield service


@pytest.fixture
def book_controller(book_service):
    controller = BookController(
        service=book_service
    )

    yield controller
