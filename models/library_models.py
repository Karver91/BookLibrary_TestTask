import traceback
from abc import ABC, abstractmethod
from datetime import datetime

from enums import BookStatusEnum
from views.console_view import console


class AbstractModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def validate(self):
        raise NotImplementedError


class Book(AbstractModel):
    def __init__(self, id: int, title: str, author: str, year: str, status: BookStatusEnum = None):
        self.id = id  # Решено отказаться от uuid, т.к. в консоль удобней вводить небольшие числа при поиске книги
        self.title = title
        self.author = author
        self.year = year
        self.status = BookStatusEnum.AVAILABLE.value if not status else status

        self.validate()

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    def validate(self):
        if not isinstance(self.id, int) or self.id < 0:
            raise ValueError("ID должен относится к типу int и быть больше нуля")
        for value in (self.title, self.author, self.year, self.status):
            self.__validate_len_value(value=value)
        self.__validate_is_not_digit('Автор', self.author)
        self.__validate_year_is_before_current()

    @staticmethod
    def __validate_len_value(value):
        if len(value) < 1:
            raise ValueError('Поля не заполнены')

    @staticmethod
    def __validate_is_not_digit(key, value):
        if any(char.isdigit() for char in value):
            raise ValueError(f'Поле {key} не должно содержать чисел')

    def __validate_year_is_before_current(self):
        if not self.year.isdigit():
            raise ValueError('Год издания должен быть числом')
        year = int(self.year)
        current_year = datetime.now().year
        if year > current_year:
            raise ValueError('Год издания должен быть меньше текущего')
