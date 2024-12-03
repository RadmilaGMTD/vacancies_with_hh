from abc import ABC, abstractmethod
import requests

class Parser(ABC):

    @abstractmethod
    def _connection_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class HeadHunterAPI(Parser):
    def __init__(self):
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 0}
        self.__vacancies = []

    def _connection_to_api(self):
        """Инициализирует класс HeadHunterAPI и задает начальные параметры."""
        response = requests.get(url='https://api.hh.ru/vacancies', headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            raise ValueError("Не удалось получить вакансии")
        else:
            return response.json()

    def get_vacancies(self, keyword, max_pages=20):
        """Устанавливает соединение с API HeadHunter."""
        self.__params['text'] = keyword
        self.__params['per_page'] = 100

        while self.__params['page'] != max_pages:
            response = self._connection_to_api()
            self.__vacancies += response.get('items', [])
            self.__params['page'] += 1
        return self.__vacancies


# if __name__ == "__main__":
#     hh = HeadHunterAPI()
#     print(hh.get_vacancies('Python Junior'))
