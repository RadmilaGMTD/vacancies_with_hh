from src.vacancy import Vacancy
import pytest


@pytest.fixture
def vacancy_1():
    return {'name': 'Инженер-программист junior', 'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
                                                   'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
                                                   'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
                                                   'schedule': {'name': 'Удаленная работа'},
                                                   'experience': {'name': 'От 1 года до 3 лет'},
                                                   'employment': {'name': 'Полная занятость'}}



@pytest.fixture
def vacancy_obj():
    return Vacancy("Python Junior", 50000, 80000, "Требования", "удаленно", "Знание Phyton", "https://api.hh.ru/vacancies/108168182?host=hh.ru")


@pytest.fixture
def vacancy_obj_2():
    return Vacancy("Python Junior", 40000, 80000, "Требования", "удаленно", "Знание Phyton", "https://api.hh.ru/vacancies/108168182?host=hh.ru")


@pytest.fixture
def list_of_vacancies():
    return [{'name': 'junior', 'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
            'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
            'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
            'schedule': {'name': 'Удаленная работа'},
            'experience': {'name': 'От 1 года до 3 лет'},
             'employment': {'name': 'Полная занятость'}},
            {'name': 'Python junior', 'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
             'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
             'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
             'schedule': {'name': 'Удаленная работа'},
             'experience': {'name': 'От 1 года до 3 лет'},
             'employment': {'name': 'Полная занятость'}},
            {'name': 'Python', 'salary': "Не указано",
             'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
             'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
             'schedule': {'name': 'Удаленная работа'},
             'experience': {'name': 'От 1 года до 3 лет'},
             'employment': {'name': 'Полная занятость'}}
            ]