import json
from src.API.vacancy_api import HeadHunterAPI
from src.Model.vacancy import Vacancy
from src.Utils.utils import filter_vacancies, get_top_vacancies, write_vacancies_to_file, sort_vacancies, \
    print_vacancies


class JSONSaver:
    @staticmethod
    def save_to_json(vacancies, filename):
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump([vars(vacancy) for vacancy in vacancies], json_file, ensure_ascii=False, indent=4)


def get_user_input(prompt, validator=None):
    while True:
        user_input = input(prompt)
        if validator is None or validator(user_input):
            return user_input
        print("Пожалуйста, введите корректное значение.")


def get_positive_integer(prompt):
    def is_positive_integer(input_str):
        try:
            num = int(input_str)
            return num > 0
        except ValueError:
            return False

    return int(get_user_input(prompt, is_positive_integer))


def get_salary_range():
    salary_range = input("\033[91mВведите диапазон зарплат (Пример: 100000 - 150000):\033[0m ")
    if salary_range.strip():
        return map(int, salary_range.split('-'))
    return None, None


def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("\033[91mВведите поисковый запрос:\033[0m ")
    hh_vacancies_data = hh_api.get_vacancies(search_query)

    if hh_vacancies_data:
        print(f"Найдено {len(hh_vacancies_data)} вакансий:")
        vacancies_list = Vacancy.cast_to_object_list(hh_vacancies_data)

        top_n = get_positive_integer("\033[91mВведите количество вакансий для вывода в топ №:\033[0m ")

        filter_words = input("\033[91mВведите ключевые слова для фильтрации вакансий "
                             "(разделенные пробелом):\033[0m ").split()

        salary_min, salary_max = get_salary_range()

        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        if salary_min is not None and salary_max is not None:
            filtered_vacancies = [v for v in filtered_vacancies if
                                  v.salary is not None and salary_min <= v.salary <= salary_max]

        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

        if top_vacancies:
            print("Топ", top_n, "вакансий:")
            print_vacancies(top_vacancies)

            write_vacancies_to_file(top_vacancies, 'top_vacancies.txt')
            JSONSaver.save_to_json(top_vacancies, 'top_vacancies.json')
            print("Результаты были записаны в файлы 'top_vacancies.txt' и 'top_vacancies.json'")
        else:
            print("Не удалось найти вакансии, соответствующие вашим критериям.")
    else:
        print("Не удалось получить вакансии по вашему запросу.")


if __name__ == "__main__":
    user_interaction()
    print("Программа завершила выполнение.")
