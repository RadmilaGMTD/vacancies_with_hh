import unittest
from unittest.mock import patch, Mock
import requests
from src.hh_api import HeadHunterAPI
import pytest

class TestHeadHunterAPI(unittest.TestCase):
    @patch("src.hh_api.requests.get")
    def test__connection_to_api(self, mock_get: Mock):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'name': 'Инженер-программист junior', 'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
                                                   'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
                                                   'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
                                                   'schedule': {'name': 'Удаленная работа'},
                                                   'experience': {'name': 'От 1 года до 3 лет'},
                                                   'employment': {'name': 'Полная занятость'}}
        hh = HeadHunterAPI()
        assert hh._connection_to_api() == {'name': 'Инженер-программист junior', 'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
                                                   'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
                                                   'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
                                                   'schedule': {'name': 'Удаленная работа'},
                                                   'experience': {'name': 'От 1 года до 3 лет'},
                                                   'employment': {'name': 'Полная занятость'}}

    @patch("src.hh_api.requests.get")
    def test__connection_to_api_error(self, mock_get: Mock):
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = {'name': 'Инженер-программист junior',
                                                   'salary': {'from': 110000, 'to': None, 'currency': 'RUR'},
                                                   'url': 'https://api.hh.ru/vacancies/111986458?host=hh.ru',
                                                   'snippet': {'requirement': 'Опыт программирования на любом из языков ООП'},
                                                   'schedule': {'name': 'Удаленная работа'},
                                                   'experience': {'name': 'От 1 года до 3 лет'},
                                                   'employment': {'name': 'Полная занятость'}}
        hh = HeadHunterAPI()
        with self.assertRaises(ValueError):
            hh._connection_to_api()