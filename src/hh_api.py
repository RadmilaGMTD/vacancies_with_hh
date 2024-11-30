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
        self.__vacancies = []
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 0}

    def _connection_to_api(self):
        response = requests.get(url='https://api.hh.ru/vacancies', headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            return []
        else:
            return response.json()

    def get_vacancies(self, keyword):
        self.__params['text'] = keyword
        self.__params['per_page'] = 1

        while self.__params['page'] != 5:
            response = self._connection_to_api()
            self.__vacancies += response['items']
            self.__params['page'] += 1
        # for i in self.__vacancies:
        #     self.__result.append({'name': i['name'],
        #                    'salary_to': i['salary']['to'] if i['salary']['to'] else "Not specified",
        #                    'salary_from': i['salary']['from'] if i['salary']['from'] else 'Not specified',
        #                    "experience": i["experience"]["name"],
        #                    "schedule": i["schedule"]["name"],
        #                    "date": i["published_at"][:10],
        #                    'url': i['url']})
        return self.__vacancies
#
# hh = HeadHunterAPI()
# print(hh.get_vacancies('Python Junior'))