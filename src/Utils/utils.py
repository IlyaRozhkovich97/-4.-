import requests
import re


def sort_vacancies(vacancies):
    """
    Сортирует список вакансий.

    """
    return sorted(vacancies, key=lambda x: x.name)


def filter_vacancies(vacancies, filter_words):
    """
    Фильтрует список вакансий на основе списка ключевых слов.

    """
    return [vacancy for vacancy in vacancies if
            all(word.lower() in vacancy.name.lower() for word in filter_words)]


def get_top_vacancies(vacancies, n):
    """
    Получает топ N вакансий из списка вакансий.

    """
    return vacancies[:n]


def fetch_vacancy_description(vacancy):
    """
    Получает описание вакансии по ссылке.

    """
    if hasattr(vacancy, 'url'):
        response = requests.get(vacancy.url)
        if response.status_code == 200:
            vacancy_data = response.json()
            if 'description' in vacancy_data and vacancy_data['description']:
                description = vacancy_data['description']
            else:
                description = vacancy.description if hasattr(vacancy, 'description') else 'Описание не указано'
            return re.sub('<[^<]+?>', '', description)
        else:
            return "Не удалось получить данные по ссылке"
    else:
        return "Описание: Описание не указано"


def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях.

    """
    for vacancy in vacancies:
        print(f"Вакансия: {vacancy.name}\nЗарплата: {vacancy.salary} {vacancy.currency}")
        if hasattr(vacancy, 'experience'):
            print(f"Опыт работы: {vacancy.experience['name']}")
        print(f"Ссылка: {vacancy.url if hasattr(vacancy, 'url') else 'Не указана'}")

        description = fetch_vacancy_description(vacancy)
        print(f"Описание: {description}\n")


def write_vacancies_to_file(vacancies, filename):
    """
    Записывает информацию о вакансиях в файл.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        for vacancy in vacancies:
            file.write(f"Вакансия: {vacancy.name}\n")
            file.write(f"Зарплата: {vacancy.salary} {vacancy.currency}\n")
            if hasattr(vacancy, 'experience') and vacancy.experience:
                experience_name = vacancy.experience.get('name', 'Не указан')
                file.write(f"Опыт работы: {experience_name}\n")
            file.write(f"Ссылка: {vacancy.url if hasattr(vacancy, 'url') else 'Не указана'}\n")

            description = fetch_vacancy_description(vacancy)
            file.write(f"Описание: {description}\n\n")
