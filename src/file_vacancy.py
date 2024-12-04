# from src.vacancy import Vacancy
# from src.hh_api import HeadHunterAPI
# from src.utils import salary_range
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

    def __init__(self, file: str = "../data/vacancies.json") -> None:
        """Инициализирует класс JsonFile и задает начальные параметры."""
        self.__file = file

    def get_data_file(self) -> Any:
        """Получение данных из файла."""
        full_path = os.path.abspath(self.__file)
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {full_path}")
        except json.JSONDecodeError:
            return []

    def add_data_file(self, vacancy_list: list) -> None:
        """Добавление данных в файл."""
        read_data = self.get_data_file()
        full_path = os.path.abspath(self.__file)
        if not read_data:
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(vacancy_list, f, ensure_ascii=False, indent=4)
        else:
            for vacancy in vacancy_list:
                if vacancy in read_data:
                    continue
                read_data.append(vacancy)
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(read_data, f, ensure_ascii=False, indent=4)

    def delete_data_file(self, vacancy_delete_url: str) -> None:
        """Удаление данных из файла по URL вакансии."""
        read_data = self.get_data_file()
        full_path = os.path.abspath(self.__file)
        read_data = [vacancy for vacancy in read_data if vacancy.get("url") != vacancy_delete_url]
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(read_data, f, ensure_ascii=False, indent=4)


# if __name__ == "__main__":
#     vacan = Vacancy("Python Developer", 50000, 90000, "Опыт", "удаленно", "Требования",
#     "https://api.hh.ru/vacancies/110091946?host=hh.ru")
#     path = '../data/vacancies.json'
#     json_file = JsonFile(path)
#     list_vacancies = HeadHunterAPI()
#     filtered_vacancies = vacan.cast_to_object_list(list_vacancies.get_vacancies("Python Junior"))
#     salary_filter_vacancies = salary_range(50000, filtered_vacancies)
#     json_file.add_data_file(salary_filter_vacancies)
#     json_file.delete_data_file("https://api.hh.ru/vacancies/110281913?host=hh.ru")
