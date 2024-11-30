from src.hh_api import HeadHunterAPI

class Vacancy:
    """Класс для описания вакансии"""
    __slots__ = ("__name", "__salary_from", "__salary_to", "__experience", "__schedule", "__snippet", "__url")

    def __init__(self, name, salary_from, salary_to, experience, schedule, snippet, url):
        """Инициализация экземпляра вакансии."""
        self.__name = self.__validation_name(name)
        self.__salary_to = self.__validation_salary(salary_to)
        self.__salary_from = self.__validation_salary(salary_from)
        self.__experience = self.__validation_experience(experience)
        self.__schedule = self.__validation_schedule(schedule)
        self.__snippet = self.__validation_snippet(snippet)
        self.__url = self.__validation_url(url)

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def name(self):
        return self.__name

    @property
    def experience(self):
        return self.__experience

    @property
    def schedule(self):
        return self.__schedule

    @property
    def snippet(self):
        return self.__snippet

    @property
    def url(self):
        return self.__url

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary_from} - {self.salary_to}, Experience: {self.experience}, Schedule: {self.schedule}, Snippet: {self.snippet}, URL: {self.url}"

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    @staticmethod
    def __validation_salary(salary):
        if salary is None or (isinstance(salary, str)):
            return "Зарплата не указана"
        elif isinstance(salary, int) and salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        return salary

    @staticmethod
    def __validation_name(name):
        if not name:
            return "Название вакансии не указано"
        return name

    @staticmethod
    def __validation_experience(experience):
        if not experience:
            return "Опыт работы в вакансии не указано"
        return experience

    @staticmethod
    def __validation_schedule(schedule):
        if not schedule:
            return "Формат работы в вакансии не указано"
        return schedule


    @staticmethod
    def __validation_snippet(snippet):
        if not snippet:
            return "Требования к сотруднику в вакансии не указаны"
        return snippet

    @staticmethod
    def __validation_url(url):
        if not url:
            return "Ссылка на вакансию не указана"
        return url


    @classmethod
    def cast_to_object_list(cls, list_of_vacancies):
        filter_vacancies = []
        for vacancies in list_of_vacancies:
            salary_info = cls.__validation_salary(vacancies.get("salary", {}))
            if isinstance(salary_info, str):
                salary_from = "Зарплата не указана"
                salary_to = "Зарплата не указана"
            else:
                salary_from = cls.__validation_salary(salary_info.get("from"))
                salary_to = cls.__validation_salary(salary_info.get("to"))
                if salary_info.get("currency") != "RUR":
                    continue
            vacancy = Vacancy(
                name=vacancies.get("name", "Not specified"),
                salary_from=salary_from,
                salary_to=salary_to,
                experience=vacancies.get("experience", {}).get("name", "Not specified"),
                schedule=vacancies.get("schedule", {}).get("name", "Not specified"),
                snippet=vacancies.get("snippet", {}).get("requirement", "Not specified"),
                url=vacancies.get("url", "Not specified")
            )
            filter_vacancies.append(vacancy)

        return filter_vacancies




vacan = Vacancy("Python Developer", 100000, 123, "Требования", "удаленно", "", "")
l_v = HeadHunterAPI()
filtered_vacancies = vacan.cast_to_object_list(l_v.get_vacancies("Python Junior"))
for v in filtered_vacancies:
    print(v)
