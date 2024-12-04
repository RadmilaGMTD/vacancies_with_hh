from abc import ABC, abstractmethod
from typing import Any

import requests


class Parser(ABC):
    """Абстрактный класс для работы с апи"""

    @abstractmethod
    def _connection_to_api(self) -> Any:
        """Устанавливает соединение с API HeadHunter."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, max_pages: int = 20) -> list:
        """Получает необходимые вакансии по ключевому слову."""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с апи"""

    def __init__(self) -> None:
        """Инициализирует класс HeadHunterAPI и задает начальные параметры."""
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 0}
        self.__vacancies: list = []

    def _connection_to_api(self) -> Any:
        """Устанавливает соединение с API HeadHunter."""
        response = requests.get(url="https://api.hh.ru/vacancies", headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            raise ValueError("Не удалось получить вакансии")
        else:
            return response.json()

    def get_vacancies(self, keyword: str, max_pages: int = 20) -> list:
        """Получает необходимые вакансии по ключевому слову."""
        self.__params["text"] = f'"{keyword}"'
        self.__params["per_page"] = 100

        while self.__params["page"] != max_pages:
            response = self._connection_to_api()
            self.__vacancies += response.get("items", [])
            self.__params["page"] += 1
        return self.__vacancies


# if __name__ == "__main__":
#     hh = HeadHunterAPI()
#     print(hh.get_vacancies('Python Junior'))
