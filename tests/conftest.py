import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1() -> dict:
    return {
        "name": "Инженер-программист junior",
        "salary": {"from": 110000, "to": None, "currency": "RUR"},
        "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
        "snippet": {"requirement": "Опыт программирования на любом из языков ООП"},
        "schedule": {"name": "Удаленная работа"},
        "experience": {"name": "От 1 года до 3 лет"},
        "employment": {"name": "Полная занятость"},
    }


@pytest.fixture
def vacancy_obj() -> Vacancy:
    return Vacancy(
        "Python Junior",
        50000,
        80000,
        "Требования",
        "удаленно",
        "Знание Phyton",
        "https://api.hh.ru/vacancies/108168182?host=hh.ru",
    )


@pytest.fixture
def vacancy_obj_2() -> Vacancy:
    return Vacancy(
        "Python Junior",
        40000,
        80000,
        "Требования",
        "удаленно",
        "Знание Phyton",
        "https://api.hh.ru/vacancies/108168182?host=hh.ru",
    )


@pytest.fixture
def list_of_vacancies() -> list:
    return [
        {
            "name": "junior",
            "salary": {"from": 110000, "to": None, "currency": "RUR"},
            "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
            "snippet": {"requirement": "Опыт программирования на любом из языков ООП"},
            "schedule": {"name": "Удаленная работа"},
            "experience": {"name": "От 1 года до 3 лет"},
            "employment": {"name": "Полная занятость"},
        },
        {
            "name": "Python junior",
            "salary": {"from": 110000, "to": None, "currency": "RUR"},
            "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
            "snippet": {"requirement": "Опыт программирования на любом из языков ООП"},
            "schedule": {"name": "Удаленная работа"},
            "experience": {"name": "От 1 года до 3 лет"},
            "employment": {"name": "Полная занятость"},
        },
        {
            "name": "Python",
            "salary": "Не указано",
            "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
            "snippet": {"requirement": "Опыт программирования на любом из языков ООП"},
            "schedule": {"name": "Удаленная работа"},
            "experience": {"name": "От 1 года до 3 лет"},
            "employment": {"name": "Полная занятость"},
        },
    ]


@pytest.fixture
def list_of_vacancies_obg() -> list:
    return [
        {
            "name": "junior",
            "salary_from": 110000,
            "salary_to": "Зарплата не указана",
            "experience": "От 1 года до 3 лет",
            "schedule": "Удаленная работа",
            "snippet": "Опыт программирования на любом из языков ООП",
            "url": "https://api.hh.ru/vacancies/111986488?host=hh.ru",
        },
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
