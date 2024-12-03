import unittest
from unittest.mock import patch, Mock

from src.vacancy import Vacancy
from tests.conftest import vacancy_obj
import pytest


class TestVacancy:
    def test_str(self, vacancy_obj):
        expected_str = 'Name: Python Junior, Salary: 50000 - 80000, Experience: Требования, Schedule: удаленно, Snippet: Знание Phyton, URL: https://api.hh.ru/vacancies/108168182?host=hh.ru'
        assert str(vacancy_obj) == expected_str

    def test_salary_from(self, vacancy_obj):
        assert vacancy_obj.salary_from == 50000

    def test_salary_to(self, vacancy_obj):
        assert vacancy_obj.salary_to == 80000

    def test_salary_name(self, vacancy_obj):
        assert vacancy_obj.name == "Python Junior"

    def test_experience(self, vacancy_obj):
        assert vacancy_obj.experience == "Требования"

    def test_schedule(self, vacancy_obj):
        assert vacancy_obj.schedule == "удаленно"

    def test_snippet(self, vacancy_obj):
        assert vacancy_obj.snippet == "Знание Phyton"

    def test_url(self, vacancy_obj):
        assert vacancy_obj.url == "https://api.hh.ru/vacancies/108168182?host=hh.ru"

    def test___ge__(self, vacancy_obj, vacancy_obj_2):
        assert vacancy_obj >= vacancy_obj_2

    @staticmethod
    def test___validation_name(vacancy_obj):
        result = vacancy_obj._Vacancy__validation_name(name="")
        assert result == "Название вакансии не указано"
        result = vacancy_obj._Vacancy__validation_name(name="Python")
        assert result == "Python"

    @staticmethod
    def test___validation_salary(vacancy_obj):
        result = vacancy_obj._Vacancy__validation_salary(salary="")
        assert result == "Зарплата не указана"
        result = vacancy_obj._Vacancy__validation_salary(salary="stroke")
        assert result == "Зарплата не указана"
        result = vacancy_obj._Vacancy__validation_salary(salary=50000)
        assert result == 50000
        with pytest.raises(ValueError):
            vacancy_obj._Vacancy__validation_salary(salary=-5)

    @staticmethod
    def test___validation_experience(vacancy_obj):
        result = vacancy_obj._Vacancy__validation_experience(experience="")
        assert result == "Опыт работы в вакансии не указан"
        result = vacancy_obj._Vacancy__validation_experience(experience="Python")
        assert result == "Python"

    @staticmethod
    def test___validation_schedule(vacancy_obj):
        result = vacancy_obj._Vacancy__validation_schedule(schedule="")
        assert result == "Формат работы в вакансии не указан"
        result = vacancy_obj._Vacancy__validation_schedule(schedule="Python")
        assert result == "Python"

    @staticmethod
    def test___validation_snippet(vacancy_obj):
        result = vacancy_obj._Vacancy__validation_snippet(snippet="")
        assert result == "Требования к сотруднику в вакансии не указаны"
        result = vacancy_obj._Vacancy__validation_snippet(snippet="Python")
        assert result == "Python"

    @staticmethod
    def test___validation_url(vacancy_obj):
        result = vacancy_obj._Vacancy__validation_url(url="")
        assert result == "Ссылка на вакансию не указана"
        result = vacancy_obj._Vacancy__validation_url(url="Python")
        assert result == "Python"

    @classmethod
    def test_cast_to_object_list(cls, list_of_vacancies):
        assert Vacancy.cast_to_object_list(list_of_vacancies) == [{'name': 'junior', 'salary_from': 110000, 'salary_to': 'Зарплата не указана', 'experience': 'От 1 года до 3 лет', 'schedule': 'Удаленная работа', 'snippet': 'Опыт программирования на любом из языков ООП', 'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru'},
{'name': 'Python junior', 'salary_from': 110000, 'salary_to': 'Зарплата не указана', 'experience': 'От 1 года до 3 лет', 'schedule': 'Удаленная работа', 'snippet': 'Опыт программирования на любом из языков ООП', 'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru'},
                                                                  {'name': 'Python', 'salary_from': "Зарплата не указана", 'salary_to': 'Зарплата не указана', 'experience': 'От 1 года до 3 лет', 'schedule': 'Удаленная работа', 'snippet': 'Опыт программирования на любом из языков ООП', 'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru'}]

