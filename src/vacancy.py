# from src.hh_api import HeadHunterAPI
from typing import Any, Union


class Vacancy:
    """Класс для описания вакансии"""

    __slots__ = ("__name", "__salary_from", "__salary_to", "__experience", "__schedule", "__snippet", "__url")

    def __init__(
        self,
        name: str,
        salary_from: Union[int, str],
        salary_to: Union[int, str],
        experience: str,
        schedule: str,
        snippet: str,
        url: str,
    ) -> None:
        """Инициализация экземпляра вакансии."""
        self.__name = self.__validation_name(name)
        self.__salary_from = self.__validation_salary(salary_from)
        self.__salary_to = self.__validation_salary(salary_to)
        self.__experience = self.__validation_experience(experience)
        self.__schedule = self.__validation_schedule(schedule)
        self.__snippet = self.__validation_snippet(snippet)
        self.__url = self.__validation_url(url)

    @property
    def salary_from(self) -> Any:
        """Возвращает минимальную зарплату."""
        return self.__salary_from

    @property
    def salary_to(self) -> Any:
        """Возвращает максимальную зарплату."""
        return self.__salary_to

    @property
    def name(self) -> str:
        """Возвращает название вакансии."""
        return self.__name

    @property
    def experience(self) -> str:
        """Возвращает опыт работы для вакансии."""
        return self.__experience

    @property
    def schedule(self) -> str:
        """Возвращает график работы."""
        return self.__schedule

    @property
    def snippet(self) -> str:
        """Возвращает требования к кандидату."""
        return self.__snippet

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию."""
        return self.__url

    def __str__(self) -> str:
        """Строковое отображение экземпляра вакансии"""
        return (
            f"Name: {self.name}, Salary: {self.salary_from} - {self.salary_to}, "
            f"Experience: {self.experience}, Schedule: {self.schedule}, "
            f"Snippet: {self.snippet}, URL: {self.url}"
        )

    def __ge__(self, other: "Vacancy") -> Any:
        """Метод сравнения вакансий по минимальной зарплате"""
        return self.salary_from >= other.salary_from

    @staticmethod
    def __validation_salary(salary: Union[int, str]) -> Any:
        """Валидация зарплаты"""
        if salary is None or (isinstance(salary, str)):
            return "Зарплата не указана"
        elif isinstance(salary, int) and salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        return salary

    @staticmethod
    def __validation_name(name: str) -> str:
        """Валидация названия вакансии"""
        if not name:
            return "Название вакансии не указано"
        return name

    @staticmethod
    def __validation_experience(experience: str) -> str:
        """Валидация опыта работы"""
        if not experience:
            return "Опыт работы в вакансии не указан"
        return experience

    @staticmethod
    def __validation_schedule(schedule: str) -> str:
        """Валидация формата работы"""
        if not schedule:
            return "Формат работы в вакансии не указан"
        return schedule

    @staticmethod
    def __validation_snippet(snippet: str) -> str:
        """Валидация требований к сотруднику"""
        if not snippet:
            return "Требования к сотруднику в вакансии не указаны"
        return snippet

    @staticmethod
    def __validation_url(url: str) -> str:
        """Валидация ссылки на вакансию"""
        if not url:
            return "Ссылка на вакансию не указана"
        return url

    @classmethod
    def currency(cls, list_of_vacancies: list, currency: str = "RUR") -> list:
        """Функция для фильтрации по валютам"""
        my_list = []
        for vacancy in list_of_vacancies:
            salary_info = cls.__validation_salary(vacancy.get("salary", {}))
            if isinstance(salary_info, str):
                my_list.append(vacancy)
            else:
                if salary_info.get("currency") == currency:
                    my_list.append(vacancy)
        return my_list

    @classmethod
    def cast_to_object_list(cls, list_of_vacancies: list, currency: str = "RUR") -> list:
        """Преобразует список вакансий в список объектов Vacancy."""
        currency_vacancies_filter = cls.currency(list_of_vacancies, currency)
        filter_vacancies = []
        for vacancies in currency_vacancies_filter:
            salary_info = cls.__validation_salary(vacancies.get("salary", {}))
            if isinstance(salary_info, str):
                salary_from = "Зарплата не указана"
                salary_to = "Зарплата не указана"
            else:
                salary_from = cls.__validation_salary(salary_info.get("from"))
                salary_to = cls.__validation_salary(salary_info.get("to"))

            vacancy = Vacancy(
                name=vacancies.get("name", "Not specified"),
                salary_from=salary_from,
                salary_to=salary_to,
                experience=vacancies.get("experience", {}).get("name", "Not specified"),
                schedule=vacancies.get("schedule", {}).get("name", "Not specified"),
                snippet=vacancies.get("snippet", {}).get("requirement", "Not specified"),
                url=vacancies.get("url", "Not specified"),
            )

            filter_vacancies.append(vacancy.to_dict())

        return filter_vacancies

    def to_dict(self) -> dict:
        """Преобразование объекта Vacancy в словарь для дальнейшей записи в Json файл"""
        return {
            "name": self.name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "experience": self.experience,
            "schedule": self.schedule,
            "snippet": self.snippet,
            "url": self.url,
        }


# if __name__ == "__main__":
#     vacan = Vacancy("Python Junior", 50000, 80000, "Требования", "удаленно", "", "")
#     list_vacancies = HeadHunterAPI()
#     filtered_vacancies = vacan.cast_to_object_list(list_vacancies.get_vacancies("Python Junior"), "RUR")
#     for vacancies in filtered_vacancies:
#         print(vacancies)
