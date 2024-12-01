from src.vacancy import Vacancy
from src.hh_api import HeadHunterAPI
import pandas as pd


def salary_range(salary: int, filter_vacancies: list) -> list:
    """Фильтрация вакансий по минимальной зарплате."""
    res_salary = []
    for vacancies in filter_vacancies:
        salary_from = vacancies.get("salary_from")
        if isinstance(salary_from, str):
            salary_from = 0
        elif salary_from is None:
            salary_from = 0
        if salary <= salary_from:
            res_salary.append(vacancies)
    return res_salary


def top_n(filter_vacancies_salary: list, number: int) -> list:
    """Получение топ N вакансий по минимальной зарплате."""
    sorted_salary = sorted(filter_vacancies_salary, key=lambda i: i.get("salary_from"), reverse=True)
    df = pd.DataFrame(sorted_salary)
    if number > len(df):
        number = len(df)
    top_n_df = df.head(number)
    top_n_df_dict = top_n_df.to_dict(orient="records")
    return top_n_df_dict




# vacan = Vacancy("Python Junior", 50000, 80000, "Требования", "удаленно", "", "")
# hh = HeadHunterAPI()
# filtered_vacancies = vacan.cast_to_object_list(hh.get_vacancies("Python Junior"))
# salary_filter_vacancies = salary_range(50000,filtered_vacancies)
# print(salary_filter_vacancies)
# print(top_n(salary_filter_vacancies, 2))
