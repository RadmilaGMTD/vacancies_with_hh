from src.utils import salary_range, top_n


def test_salary_range(list_of_vacancies_obg: list) -> None:
    """Корректная работа функции фильтрации вакансий по зарплате"""
    assert salary_range(10000, list_of_vacancies_obg) == [
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
    ]


def test_top_n(list_of_vacancies_obg: list) -> None:
    """Корректная работа функции вывода топ вакансий"""
    assert top_n(list_of_vacancies_obg, 2) == [
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
    ]


def test_top_n_len_more(list_of_vacancies_obg: list) -> None:
    """Работа функции, если number больше вакансий"""
    assert top_n(list_of_vacancies_obg, 4) == list_of_vacancies_obg
