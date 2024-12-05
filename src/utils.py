from typing import Any

import pandas as pd


def salary_range(salary: int, filter_vacancies: list) -> list:
    """Фильтрация вакансий по минимальной зарплате."""
    res_salary = []
    for vacancies in filter_vacancies:
        salary_from = vacancies.get("salary_from", 0)
        if isinstance(salary_from, str):
            salary_from = 0
        if salary <= salary_from:
            res_salary.append(vacancies)
    return res_salary


def top_n(filter_vacancies_salary: list, number: int) -> list[Any]:
    """Получение топ N вакансий по минимальной зарплате."""
    sorted_salary = sorted(
        filter_vacancies_salary,
        key=lambda i: (int(i.get("salary_from", 0)) if str(i.get("salary_from", 0)).isdigit() else 0),
        reverse=True,
    )
    df = pd.DataFrame(sorted_salary)
    if number > len(df):
        number = len(df)
    top_n_df = df.head(number)
    top_n_df_dict = top_n_df.to_dict(orient="records")
    return top_n_df_dict
