import json
from abc import ABC, abstractmethod

from views.console_view import console


class BaseFileManager(ABC):
    """Базовый класс для работы с файлом данных"""
    def __init__(self, model, data_path):
        self.model = model
        self.data_path = data_path
        self.data = self.read_file()

    @abstractmethod
    def read_file(self) -> list:
        """Читает файл. Возвращает список объектов модели"""
        raise NotImplementedError

    @abstractmethod
    def write_file(self) -> None:
        """Записывает данные в файл"""
        raise NotImplementedError

    def generate_id(self) -> int:
        """Генерирует новый id"""
        try:
            _id = 1
            if self.data:
                _id = max([item.id for item in self.data]) + 1
            return _id
        except AttributeError:
            raise AttributeError(f'Ошибка генерации id, не найден атрибут id')


    def add_data_obj(self, obj):
        self.data.append(obj)
        self.write_file()

    def remove_data_obj(self, obj):
        try:
            self.data.remove(obj)
            self.write_file()
        except ValueError:
            raise ValueError('Объект не обнаружен в базе')


class JSONFileManager(BaseFileManager):
    """Отвечает за работу с JSON-файлом данных"""
    def __init__(self, model, data_path):
        super().__init__(model, data_path)

    def read_file(self) -> list:
        """Читает файл. Возвращает список объектов модели"""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [self.model(**item) for item in data]
        except FileNotFoundError:
            console.print_message(f'Файл {self.data_path} не найден')
            return []


    def write_file(self) -> None:
        """Записывает данные в файл"""
        with open(self.data_path, 'w', encoding='utf-8') as file:
            items = [item.to_dict() for item in self.data]
            json.dump(obj=items, fp=file, ensure_ascii=False, indent=4)
