from src.hh_api import HeadHunterAPI
from src.utils import salary_range, top_n
from src.vacancy import Vacancy


def user_interaction() -> list:
    """Функция для взаимодействия с пользователем, получения вакансий на основе его запроса."""
    search_query = input("Какая профессия Вас интересует?: ")
    top_n_user = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range_user = input("Какую зарплату Вы бы хотели?. Если зарплата не имеет значение, введите любую букву: ")
    if salary_range_user.isdigit():
        currency_user = input("В какой валюте ожидаете зарплату?: ")
        hh = HeadHunterAPI()
        filtered_vacancies = Vacancy.cast_to_object_list(hh.get_vacancies(search_query), currency_user)
        salary_filter_vacancies = salary_range(int(salary_range_user), filtered_vacancies)
        return top_n(salary_filter_vacancies, top_n_user)
    else:
        hh = HeadHunterAPI()
        filtered_vacancies = Vacancy.cast_to_object_list(hh.get_vacancies(search_query))
        return top_n(filtered_vacancies, top_n_user)


if __name__ == "__main__":
    print(user_interaction())
