from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.utils import salary_range
from src.utils import top_n



def user_interaction():
    """Функция для взаимодействия с пользователем, получения вакансий на основе его запроса."""
    search_query = input("Какая профессия Вас интересует?: ")
    top_n_user = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range_user = int(input("Какую зарплату Вы бы хотели: "))
    hh = HeadHunterAPI()
    filtered_vacancies = Vacancy.cast_to_object_list(hh.get_vacancies(search_query))
    salary_filter_vacancies = salary_range(salary_range_user, filtered_vacancies)
    return top_n(salary_filter_vacancies, top_n_user)

# print(user_interaction())
