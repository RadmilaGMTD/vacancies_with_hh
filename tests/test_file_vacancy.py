import json
import os
from unittest.mock import Mock, patch

import pytest

from src.file_vacancy import JsonFile


class TestJsonFile:
    """Класс для тестирования JsonFile"""

    def test_error_file_empty(self) -> None:
        """Ошибка при чтении файла, если файл не найден"""
        with pytest.raises(ValueError):
            JsonFile(file=None)

    @patch("src.file_vacancy.os.path.exists")
    def test_get_data_file(self, mock_exists: Mock, list_of_vacancies_obg: list) -> None:
        """Корректное чтение файла JSON"""
        mock_exists.return_value = "../test_file.json"
        rows = list_of_vacancies_obg
        json_file = JsonFile("../test_file.json")
        with open("../test_file.json", "w", encoding="UTF-8") as file:
            json.dump(rows, file)
        assert json_file.get_data_file() == rows
        os.remove("../test_file.json")

    @patch("src.file_vacancy.os.path.exists")
    def test_get_data_file_error(self, mock_exists: Mock) -> None:
        """Ошибка при чтении файла"""
        mock_exists.return_value = "../test_file.json"
        json_file = JsonFile("../test_file.json")
        with open("../test_file.json", "w") as file:
            file.write("a,s,d,f")

        assert json_file.get_data_file() == []
        os.remove("../test_file.json")

    def test_error_file(self) -> None:
        """Ошибка при чтении файла, если файл не найден"""
        with pytest.raises(FileNotFoundError):
            JsonFile(file="../test_file.json")

    @patch("src.file_vacancy.JsonFile.get_data_file")
    @patch("src.file_vacancy.os.path.exists")
    def test_add_data_file(self, mock_exists: Mock, mock_get_data_file: Mock, list_of_vacancies_obg: list) -> None:
        """Корректная работа функции записи в файл"""
        mock_exists.return_value = "../test_file.json"
        mock_get_data_file.return_value = [
            {
                "name": "junior",
                "salary_from": 110000,
                "salary_to": "Зарплата не указана",
                "experience": "От 1 года до 3 лет",
                "schedule": "Удаленная работа",
                "snippet": "Опыт программирования на любом из языков ООП",
                "url": "https://api.hh.ru/vacancies/111986488?host=hh.ru",
            }
        ]
        json_file = JsonFile("../test_file.json")
        json_file.add_data_file(list_of_vacancies_obg)
        with open("../test_file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data == list_of_vacancies_obg
        os.remove("../test_file.json")

    @patch("src.file_vacancy.JsonFile.get_data_file")
    @patch("src.file_vacancy.os.path.exists")
    def test_add_data_file_empty(
        self, mock_exists: Mock, mock_get_data_file: Mock, list_of_vacancies_obg: list
    ) -> None:
        """Корректная работа функции записи в файл, если файл пустой"""
        mock_exists.return_value = "../test_file.json"
        mock_get_data_file.return_value = []
        json_file = JsonFile("../test_file.json")
        json_file.add_data_file(list_of_vacancies_obg)
        with open("../test_file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data == list_of_vacancies_obg
        os.remove("../test_file.json")

    @patch("src.file_vacancy.JsonFile.get_data_file")
    @patch("src.file_vacancy.os.path.exists")
    def test_delete_data_file(self, mock_exists: Mock, mock_get_data_file: Mock, list_of_vacancies_obg: list) -> None:
        """Корректная работа функции удаления данных из файла"""
        mock_exists.return_value = "../test_file.json"
        mock_get_data_file.return_value = list_of_vacancies_obg
        json_file = JsonFile("../test_file.json")
        url = "https://api.hh.ru/vacancies/111986488?host=hh.ru"
        json_file.delete_data_file(url)
        with open("../test_file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data == [
            {
                "name": "Python junior",
                "salary_from": 100000,
                "salary_to": "Зарплата не указана",
                "experience": "От 1 года до 3 лет",
                "schedule": "Удаленная работа",
                "snippet": "Опыт программирования на любом из языков ООП",
                "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
            },
            {
                "name": "Python",
                "salary_from": "Зарплата не указана",
                "salary_to": "Зарплата не указана",
                "experience": "От 1 года до 3 лет",
                "schedule": "Удаленная работа",
                "snippet": "Опыт программирования на любом из языков ООП",
                "url": "https://api.hh.ru/vacancies/111986418?host=hh.ru",
            },
        ]
        os.remove("../test_file.json")
        url = "https://api.hh.ru/vacancies/111986455?host=hh.ru"
        json_file.delete_data_file(url)
        with open("../test_file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data == list_of_vacancies_obg
        os.remove("../test_file.json")
