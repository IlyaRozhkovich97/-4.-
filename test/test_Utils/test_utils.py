from src.Utils.utils import sort_vacancies, filter_vacancies, get_top_vacancies


# Создаем пример вакансий для использования в тестах
class Vacancy:
    def __init__(self, name, url, salary, currency, description, experience):
        self.name = name
        self.url = url
        self.salary = salary
        self.currency = currency
        self.description = description
        self.experience = experience


# Тесты для функции sort_vacancies
def test_sort_vacancies():
    # Создаем список вакансий
    vacancies = [
        Vacancy("Backend Developer", "https://example.com/backend", 100000, "USD", "Backend Job", {"name": "Senior"}),
        Vacancy("Frontend Developer", "https://example.com/frontend", 90000, "USD", "Frontend Job", {"name": "Junior"}),
        Vacancy("Data Scientist", "https://example.com/datascience", 120000, "USD", "Data Science Job", {"name": "Mid"})
    ]
    # Сортируем вакансии по имени
    sorted_vacancies = sort_vacancies(vacancies)
    # Проверяем, что вакансии отсортированы по алфавиту
    assert [v.name for v in sorted_vacancies] == ["Backend Developer", "Data Scientist", "Frontend Developer"]


# Тесты для функции filter_vacancies
def test_filter_vacancies():
    # Создаем список вакансий
    vacancies = [
        Vacancy("Backend Developer", "https://example.com/backend", 100000, "USD", "Backend Job", {"name": "Senior"}),
        Vacancy("Frontend Developer", "https://example.com/frontend", 90000, "USD", "Frontend Job", {"name": "Junior"}),
        Vacancy("Data Scientist", "https://example.com/datascience", 120000, "USD", "Data Science Job", {"name": "Mid"})
    ]
    # Фильтруем вакансии по ключевому слову "Developer"
    filtered_vacancies = filter_vacancies(vacancies, ["Developer"])
    # Проверяем, что только вакансии с ключевым словом "Developer" остались
    assert [v.name for v in filtered_vacancies] == ["Backend Developer", "Frontend Developer"]


# Тесты для функции get_top_vacancies
def test_get_top_vacancies():
    # Создаем список вакансий
    vacancies = [
        Vacancy("Backend Developer", "https://example.com/backend", 100000, "USD", "Backend Job", {"name": "Senior"}),
        Vacancy("Frontend Developer", "https://example.com/frontend", 90000, "USD", "Frontend Job", {"name": "Junior"}),
        Vacancy("Data Scientist", "https://example.com/datascience", 120000, "USD", "Data Science Job", {"name": "Mid"})
    ]
    # Получаем топ 2 вакансии
    top_vacancies = get_top_vacancies(vacancies, 2)
    # Проверяем, что только первые две вакансии остались
    assert len(top_vacancies) == 2
