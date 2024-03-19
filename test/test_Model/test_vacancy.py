import requests
import re


class Vacancy:
    """
    Конструктор класса Vacancy.

    """

    def __init__(self, name, url, salary, currency, description, experience):
        self.name = name
        self.url = url
        self.salary = salary
        self.currency = currency
        self.description = description
        self.experience = experience

    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        vacancies_list = []
        for vacancy in vacancies_data:
            title = vacancy.get('name', 'Название не указано')
            link = vacancy.get('url', 'Ссылка не указана')
            salary_data = vacancy.get('salary')
            if salary_data and isinstance(salary_data, dict):
                salary = salary_data.get('from', 'Зарплата не указана')
                currency = salary_data.get('currency', 'Валюта не указана')
            else:
                salary = 'Зарплата не указана'
                currency = 'Валюта не указана'

            if 'url' in vacancy:
                response = requests.get(vacancy['url'])
                if response.status_code == 200:
                    vacancy_data = response.json()
                    if 'description' in vacancy_data and vacancy_data['description']:
                        description = vacancy_data['description']
                    else:
                        description = vacancy.get('description', 'Описание не указано')

                    description = re.sub('<[^<]+?>', '', description)
                else:
                    description = 'Не удалось получить данные по ссылке'
            else:
                description = vacancy.get('description', 'Описание не указано')

            experience = vacancy.get('experience')

            vacancies_list.append(cls(title, link, salary, currency, description, experience))
        return vacancies_list
