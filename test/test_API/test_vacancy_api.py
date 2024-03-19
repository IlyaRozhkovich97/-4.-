import requests
from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    """
    Абстрактный базовый класс для API, предоставляющего доступ к вакансиям.

    """

    @abstractmethod
    def connect(self):
        """
        Абстрактный метод для подключения к API.

        """
        pass

    @abstractmethod
    def get_vacancies(self, query):
        """
        Абстрактный метод для получения списка вакансий по запросу.

        """
        pass


class HeadHunterAPI(AbstractVacancyAPI):
    """
    Класс для работы с API HeadHunter для получения информации о вакансиях.

    """

    def connect(self):
        """
        Метод для подключения к API HeadHunter.

        """
        pass

    def get_vacancies(self, query):
        """
        Метод для получения списка вакансий с использованием API HeadHunter.

        """
        base_url = "https://api.hh.ru/vacancies"
        response = requests.get(base_url, params={'text': query})
        if response.status_code == 200:
            return response.json()['items']
        else:
            return None
