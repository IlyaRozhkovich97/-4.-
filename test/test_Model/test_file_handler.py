from abc import ABC, abstractmethod
import json


class VacancyFileHandler(ABC):
    """
    Абстрактный класс для работы с файлом вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Абстрактный метод для добавления вакансии в файл.
        """
        pass

    @abstractmethod
    def get_vacancies(self, **kwargs):
        """
        Абстрактный метод для получения данных о вакансиях из файла по указанным критериям.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Абстрактный метод для удаления информации о вакансии из файла.
        """
        pass


class JSONFileHandler(VacancyFileHandler):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    """

    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        """
        Метод для добавления вакансии в JSON-файл.
        """
        with open(self.filename, 'a') as file:
            json.dump(vacancy.__dict__, file)
            file.write('\n')

    def get_vacancies(self, **kwargs):
        """
        Метод для получения данных о вакансиях из JSON-файла.
        """
        vacancies = []
        with open(self.filename, 'r') as file:
            for line in file:
                vacancy_data = json.loads(line)
                vacancies.append(vacancy_data)
        return vacancies

    def delete_vacancy(self, vacancy):
        """
        Метод для удаления информации о вакансии из JSON-файла.
        """
        vacancies = self.get_vacancies()
        updated_vacancies = [v for v in vacancies if v != vacancy]
        with open(self.filename, 'w') as file:
            for v in updated_vacancies:
                json.dump(v, file)
                file.write('\n')
