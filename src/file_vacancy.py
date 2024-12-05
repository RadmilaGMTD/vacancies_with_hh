import json
import os
from abc import ABC, abstractmethod
from typing import Any


class BaseFiles(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_data_file(self) -> list:
        """Получение данных из файла."""
        pass

    @abstractmethod
    def add_data_file(self, vacancy_list: list) -> None:
        """Добавление данных в файл."""
        pass

    @abstractmethod
    def delete_data_file(self, vacancy_delete_url: str) -> None:
        """Удаление данных из файла по URL вакансии."""
        pass


class JsonFile(BaseFiles):
    """Класс для работы с Json файлом"""

    def __init__(self, file: Any = "../data/vacancies.json") -> None:
        """Инициализирует класс JsonFile и задает начальные параметры."""
        if not file:
            raise ValueError("Файл не может быть пустым")
        self.__file = file
        self.full_path = os.path.abspath(self.__file)

        if not os.path.exists(self.full_path):
            raise FileNotFoundError(f"Файл не найден: {self.full_path}")

    def get_data_file(self) -> Any:
        """Получение данных из файла."""
        try:
            with open(self.full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError:
            return []

    def add_data_file(self, vacancy_list: list) -> None:
        """Добавление данных в файл."""
        read_data = self.get_data_file()
        if not read_data:
            with open(self.full_path, "w", encoding="utf-8") as f:
                json.dump(vacancy_list, f, ensure_ascii=False, indent=4)
        else:
            for vacancy in vacancy_list:
                if vacancy in read_data:
                    continue
                read_data.append(vacancy)
            with open(self.full_path, "w", encoding="utf-8") as f:
                json.dump(read_data, f, ensure_ascii=False, indent=4)

    def delete_data_file(self, vacancy_delete_url: str) -> None:
        """Удаление данных из файла по URL вакансии."""
        read_data = self.get_data_file()
        read_data = [vacancy for vacancy in read_data if vacancy.get("url") != vacancy_delete_url]
        with open(self.full_path, "w", encoding="utf-8") as f:
            json.dump(read_data, f, ensure_ascii=False, indent=4)
