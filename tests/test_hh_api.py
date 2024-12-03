import unittest
from unittest.mock import patch, Mock
import pytest
from src.hh_api import HeadHunterAPI
from tests.conftest import vacancy_1


class TestHeadHunterAPI:
    hh = HeadHunterAPI()
    @patch("src.hh_api.requests.get")
    def test__connection_to_api(self, mock_get: Mock, vacancy_1, ):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = vacancy_1
        result = self.hh._connection_to_api()
        assert result == vacancy_1

    @patch("src.hh_api.requests.get")
    def test__connection_to_api_error(self, mock_get: Mock):
        mock_get.return_value.status_code = 500

        with pytest.raises(ValueError):
            self.hh._connection_to_api()


    @patch("src.hh_api.HeadHunterAPI._connection_to_api")
    def test_get_vacancies(self, mock__connection_to_api: Mock, vacancy_1):
        keyword = "Python Junior"
        mock__connection_to_api.return_value  = {
            "items": [
                {
                    'name': 'Инженер-программист junior',
                    'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
                    'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
                    'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
                    'schedule': {'name': 'Удаленная работа'},
                    'experience': {'name': 'От 1 года до 3 лет'},
                    'employment': {'name': 'Полная занятость'},
                }
            ]}
        result = self.hh.get_vacancies(keyword, max_pages=1)
        assert result == [vacancy_1]


